with (import <nixpkgs> {});
mkShell {
  buildInputs = [
    python3
    python3Packages.numpy
    python3Packages.regex
    clojure
  ];
}