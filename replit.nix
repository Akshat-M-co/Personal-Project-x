{ pkgs }: {
  deps = [
    pkgs.got
    pkgs.neovim
    pkgs.unzip
    pkgs.replitPackages.prybar-python310
    pkgs.replitPackages.stderred
  ];
}