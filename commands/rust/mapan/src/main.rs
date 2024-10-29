use std::env;
use std::io::{stdin, stdout, IsTerminal, Read, Write};
use std::ops::RangeInclusive;
use std::process::exit;

const NUMERIC: RangeInclusive<char> = '0'..='9';
const ALPHALOC: RangeInclusive<char> = 'a'..='z';
const ALPHAUPC: RangeInclusive<char> = 'A'..='Z';
const SPECIAL1: RangeInclusive<char> = '!'..='/';
const SPECIAL2: RangeInclusive<char> = ':'..='@';
const SPECIAL3: RangeInclusive<char> = '['..='`';
const SPECIAL4: RangeInclusive<char> = '{'..='~';

fn from_str(s: &str) -> Vec<char> {
    let mut buffer = Vec::<char>::new();

    for c in s.chars() {
        match c {
            's' => buffer.extend(SPECIAL1.chain(SPECIAL2).chain(SPECIAL3).chain(SPECIAL4)),
            'u' => buffer.extend(ALPHAUPC),
            'l' => buffer.extend(ALPHALOC),
            'a' => buffer.extend(ALPHAUPC.chain(ALPHALOC)),
            'n' => buffer.extend(NUMERIC),
            'e' => buffer.extend(
                ALPHALOC
                    .chain(ALPHAUPC)
                    .chain(ALPHALOC)
                    .chain(NUMERIC)
                    .chain(SPECIAL1)
                    .chain(SPECIAL2)
                    .chain(SPECIAL3)
                    .chain(SPECIAL4),
            ),
            '1' => buffer.extend(SPECIAL1),
            '2' => buffer.extend(SPECIAL2),
            '3' => buffer.extend(SPECIAL3),
            '4' => buffer.extend(SPECIAL4),
            _ => {
                eprintln!(
                    "Invalid charset character '{}', available (mnemonic) : sulane1234",
                    c
                );
            }
        }
    }

    buffer
}

fn print_usage() {
    eprintln!(
        r##"   
Usage: [<charset-chars>|--help(-h)]

Examples: ..command | mapan nl1
          ..command | mapan u134
          ..command | mapan s
          ..command | mapan a

Charset Characters:
    e   | Everything
    --------------------------------------
    a   | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    u   | ABCDEFGHIJKLMNOPQRSTUVWXYZ
    l   | abcdefghijklmnopqrstuvwxyz
    --------------------------------------
    n   | 0123456789
    --------------------------------------
    s   | !"#$%&'()*+,-./:;<=>?@[\]^_`{{|}}~
    --------------------------------------
    1   | !"#$%&'()*+,-.     
    2   | :;<=>?@    
    3   | \][^_`    
    4   | }}|{{~
"##
    );
}

fn main() {
    if stdin().is_terminal() {
        eprintln!("Error: no input provided; use a pipe");
        exit(1);
    }

    let arguments: Vec<String> = env::args().skip(1).collect();

    let Some(first) = arguments.first() else {
        print_usage();
        exit(1);
    };

    if first == "--help" || first == "-h" {
        print_usage();
        exit(0);
    }

    let charset = from_str(first);

    if charset.is_empty() {
        eprintln!("Charset is empty; have no characters to work with.");
        exit(1);
    }

    let mut input_data = Vec::<u8>::new();

    if let Err(e) = stdin().read_to_end(&mut input_data) {
        eprintln!("Error, cannot read from stdin: {}", e);
        exit(1);
    }

    let mapped_output = input_data
        .iter()
        .map(|&c| charset[c as usize % charset.len()])
        .collect::<String>();

    if let Err(e) = stdout().write_all(mapped_output.as_bytes()) {
        eprintln!("Error, cannot write to stdout: {}", e);
        exit(1);
    }

    if let Err(e) = stdout().flush() {
        eprintln!("Error, cannot flush stdout: {}", e);
        exit(1);
    }

    exit(0);
}
