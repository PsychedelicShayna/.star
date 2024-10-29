use std::env::args;
use std::io::{stdin, stdout, BufReader, IsTerminal, Read, Write};
use std::process::exit;

fn main() {
    let arguments: Vec<String> = args().collect();
    let mut numbers = Vec::<u64>::new();

    for argument in arguments {
        if argument.chars().all(|c| c.is_ascii_digit()) {
            let Ok(number) = argument.parse::<u64>() else {
                eprintln!("Invalid number \"{}\"", argument);
                exit(1);
            };

            numbers.push(number);
        }
    }

    if stdin().is_terminal() {
        let Some(result) = numbers.into_iter().reduce(|acc, n| acc ^ n) else {
            eprintln!("Unable to reduce provided numbers via xor");
            exit(1);
        };

        println!("{}", result);
    } else {
        let mut buffer = Vec::<u8>::new();
        let mut reader = BufReader::new(stdin());

        if let Err(e) = reader.read_to_end(&mut buffer) {
            eprintln!("Error reading from stdin: {:?}", e);
            exit(1);
        }

        for n in numbers {
            for b in &mut buffer {
                *b ^= n as u8;
            }
        }

        let mut stdout = stdout().lock();
        if let Err(e) = stdout.write_all(&buffer) {
            eprintln!("Error writing to stdout: {:?}", e);
            exit(1);
        }

        stdout
            .flush()
            .expect("Why does somebody not know how to flush the toilet after they had a shit?");

        exit(0);
    }
}
