# img-manip

## Dependencies

- [Nix 2.0](https://nixos.org/nix/) package manager
- `direnv`, Install for instance by running `nix-env -i direnv`. Then hook into
  shell via `eval "$(direnv hook bash)"`. Change name of shell to yours, if
  necessary and add the `eval` line to `.bashrc` (or equivalent) to make it
  "persistent".


## Usage

```bash
git clone https://github.com/sveitser/img-manip
cd img-manip
direnv allow
# ...the first time this will download and install everything so takes a while
./test.py
```

See http://scikit-image.org/docs/dev/auto_examples/edges/plot_edge_filter.html for
more examples.

