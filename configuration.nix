{ ... }:

{
  nix.enable = false;

  nixpkgs.config.allowUnfree = true;
  nixpkgs.hostPlatform = "aarch64-darwin";

  system.primaryUser = "khoatran";
  users.users.khoatran = {
    home = "/Users/khoatran";
  };
  system.stateVersion = 6;

  nix-homebrew = {
    enable = true;
    user = "khoatran";
    autoMigrate = true;
  };

  homebrew = {
    enable = true;

    onActivation.cleanup = "zap";
    onActivation.autoUpdate = true;
    onActivation.extraFlags = [ "--force" ];

    brews = [
      "herdr"
      "node"
    ];

    casks = [
      "wezterm"
      "claude-code"
      "opensuperwhisper"
    ];
  };
}
