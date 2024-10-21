function goimg # Opens Google Images, searching for the specified terms.
  set -l query $argv
  set -l encoded_query "$(qpe 'import urllib.parse, sys' "urllib.parse.quote('+'.join('$query'.split())).replace('%2B', '+')")"
  set -l url "https://google.com/search?q=$encoded_query&udm=2"
  xdg-open "$url"
end
