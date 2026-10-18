# Set up WeMol CLI 1.2.0

This Skill includes a bootstrap helper, not the CLI executable. It remains loadable without `wemol-cli` and can install the CLI when the agent handles a WeMol setup/use request. No installation runs merely because ClawHub copies this Skill folder. Run setup in the environment where the agent will execute commands, not on a different desktop host.

## Agent bootstrap

1. Preserve the user's chosen executable and data-directory arguments/environment. Inspect shell resolution (`type -a wemol-cli` or `Get-Command wemol-cli -All`) before running the helper; a Python process cannot discover shell functions or aliases. Preserve any wrapper's account-specific arguments and resolve its actual executable instead of bypassing it. Do not change, copy, clear or reinitialize accounts or credentials. If an executable's origin is unknown, establish it before running it. If the user has an explicit executable path, pass it with `--existing-cli`.
2. Locate Python 3.9+ (`python3`, `python`, or `py -3` on Windows) and run the bundled helper using the actual absolute Skill directory. Paths below are examples to substitute, not literal directories:

```sh
python3 "/absolute/path/to/skill/scripts/install_cli.py"
# Select an existing installation when the user already specified it:
python3 "/absolute/path/to/skill/scripts/install_cli.py" --existing-cli "/absolute/path/to/wemol-cli"
```

In PowerShell, use `py -3 "C:\path\to\skill\scripts\install_cli.py"` when the Python launcher is available. If Python 3.9+ is absent, perform the same download, checksum and no-overwrite steps below with native tools; do not install an extra runtime just for this helper.

3. Read the JSON response. `installed` and `reused` with `compatible: true` are success. Invoke its absolute `path` with appropriate shell quoting (PowerShell uses `&`) for subsequent commands. `existing-version` preserves the existing binary and reports its version; follow the migration section without overwriting it automatically or downgrading a newer CLI. `select-existing` means multiple installations were found: use the user's known choice, or ask which installation to use, then pass `--existing-cli`. Other failures stop setup; do not run an unverified download. Unresolved cases exit nonzero even when an existing binary was successfully identified.
4. From the selected final executable, inspect its no-argument setup guidance to confirm the data directory. Preserve any existing `--data-dir` or `WEMOL_CLI_DATA_DIR`; then run `status` and `channels` with that same invocation. Do not install the embedded Skill as part of ClawHub setup. If no account exists or authentication has expired, give the user the terminal login command rather than collecting credentials.
5. Report the executable version/path and whether channels are available. A successful installation does not require a persistent PATH edit: use the full path immediately, and on later sessions the helper also checks the default install directory. Modify persistent PATH only when requested. The helper cleans download and staging files even after failure; preserve intentional backups from any separately requested upgrade.

The helper's source of truth is [cli-release.json](cli-release.json): fixed HTTPS URLs, archive sizes/hashes and executable sizes/hashes. It prefers `curl` with TLS verification, or Python's HTTPS client when curl is absent. It detects macOS ARM64/x86_64 (including Rosetta), Linux x86_64, and Windows x86_64. Unsupported architectures stop without selecting an emulated or unrelated binary. It writes only a missing executable into the user install directory using an atomic no-overwrite operation; it does not change PATH, shell profiles, services, accounts or data directories. `--install-dir` selects a different binary directory, for example an isolated test directory; it is not a data-directory option.

## Download and verify

Download from the official [WeMol CLI v1.2.0 GitHub Release](https://github.com/wecomput/wemol-cli/releases/tag/v1.2.0) using the version-pinned links below. An existing verified CLI 1.2.0 does not need another download.

Choose the archive for the environment where the agent executes commands:

| Platform | Download | Archive SHA256 |
| --- | --- | --- |
| macOS Apple Silicon | [wemol-cli-v1.2.0-macos-arm64.zip](https://github.com/wecomput/wemol-cli/releases/download/v1.2.0/wemol-cli-v1.2.0-macos-arm64.zip) | `ced0135d9f383070fe2698fd77caa36e5638e6c413ef605bd08649c8d97e3685` |
| macOS Intel | [wemol-cli-v1.2.0-macos-x86_64.zip](https://github.com/wecomput/wemol-cli/releases/download/v1.2.0/wemol-cli-v1.2.0-macos-x86_64.zip) | `6ee495b827b3b8d6e8e906c077f06d343e049cb920150c64d8473ba29b75df10` |
| Windows x86_64 | [wemol-cli-v1.2.0-windows-x86_64.zip](https://github.com/wecomput/wemol-cli/releases/download/v1.2.0/wemol-cli-v1.2.0-windows-x86_64.zip) | `4982844c9f30bf949e1b193ac130d38c1ed2690c9fc93de9593d8386ccbf4ae1` |
| Linux x86_64 (musl) | [wemol-cli-v1.2.0-linux-x86_64-musl.tar.gz](https://github.com/wecomput/wemol-cli/releases/download/v1.2.0/wemol-cli-v1.2.0-linux-x86_64-musl.tar.gz) | `aa8dcd9bd5c805603d9e36f24e7d428f42df2cec4b36a99090a765cdf98e9056` |

Checksum file: [SHA256SUMS](https://github.com/wecomput/wemol-cli/releases/download/v1.2.0/SHA256SUMS).

These are SHA256 hashes of the release archives, not of the extracted executables. Hash the downloaded archive with `shasum -a 256 <archive>` (macOS), `sha256sum <archive>` (Linux), or `Get-FileHash -Algorithm SHA256 <archive>` (PowerShell). Compare with the matching value above before extracting. Stop if it differs. These artifacts do not provide a Linux ARM64 or Windows ARM64 build; do not select an unrelated architecture.

## Install in the execution environment

Extract the selected archive and place its executable in a permanent user directory, normally `~/.local/bin/wemol-cli` on macOS/Linux or `%LOCALAPPDATA%\Programs\WeMolCLI\wemol-cli.exe` on Windows. Preserve executable permissions on macOS/Linux. Use the resulting absolute path directly; a persistent PATH change is optional and should follow the user's preference. Rust and Node.js are not required by the CLI.

Inspect an existing installation before replacing it: use `type -a wemol-cli` on macOS/Linux or `Get-Command wemol-cli -All` in PowerShell. Verify the selected final executable with `--version`; it must report `wemol-cli 1.2.0` for this edition. These packages are unsigned and not notarized; if blocked, use the OS's normal per-file approval process after verifying the source rather than disabling system-wide protections.

The CLI automatically starts its local background runtime when needed. Run it as the same system user and in the same environment as the intended accounts. A container, WSL, sandbox, or remote host needs its own accessible CLI and configuration; do not assume a desktop installation is visible there.

Preserve any existing `--data-dir` argument or `WEMOL_CLI_DATA_DIR`. Defaults are `~/Library/Application Support/WeMolCLI` on macOS, usually `~/.local/share/WeMolCLI` on Linux, and `%LOCALAPPDATA%\WeMolCLI` on Windows. Data-directory changes can select different accounts. Never copy credentials into the Skill folder.

This Skill is published as `@wecomput/wemol-cli`, with the internal name `wemol-cli-official`. Install it with `clawhub install @wecomput/wemol-cli` in the intended agent workspace, and update that owner-qualified listing thereafter. If the older `@nanomolar/wemol-cli` is installed, preserve personal edits and remove or replace its managed installation through the host before installing this edition. Both listings can target the same local `wemol-cli` folder and internal Skill name, so avoid loading both. Switching listings does not migrate CLI accounts or change either listing's ownership. Reload through the host after installation. Do not treat generic CLI setup guidance about `skill install` as a ClawHub update: that command installs the separate embedded `wemol` Skill. If both are present, choose one edition to load and preserve personal edits before retiring redundant copies.

## Login and verify access

First run `status` and `channels` using the selected executable and existing data directory. Only if a channel is missing or needs authentication, give the user the corresponding `login` command to run in their own terminal. The available commands are:

```sh
wemol-cli login
wemol-cli status
wemol-cli channels
```

`login` prompts for the platform (default `https://wemol.wecomput.com`), account, and hidden password. It selects API key or Cookie authentication according to the platform's support. An existing channel can use `login --channel "channel-name"`; `login --api-key` prompts for an existing frontend user API key. Agents must not type credentials, request them in chat, or put credential values in arguments, environment variables, or pipe input. The optional data-directory environment variable is a path, not a credential.

`status` checks the local runtime, not platform authentication. Inspect each channel's `access.state` in `channels`; an empty list means accounts still need configuration. Public document search/read does not require platform authentication, but CLI 1.2.0 still requires a configured channel. In a clean installation with no channels, it returns `no_channels`; follow the login setup rather than inventing a channel or claiming anonymous access works without one. Account access and computation require valid authentication.

Users manage accounts and policies in `wemol-cli tui`. New standalone channels default to no approval; existing policies survive upgrades. This does not authorize an agent to submit an unrequested computation. Platform computation can consume quota or incur charges under the user's account; public Skill installation does not include compute credits. Setup verification must not submit a job or change approval policy.

## Existing installations

- The previous ClawHub Skill 1.0.0 also used the name `wemol-cli-official`, but targeted legacy CLI commands (`host`, `module`, `flow`, singular `job`). Updating the Skill alone does not upgrade that CLI. Install and verify CLI 1.2.0 first, then reload this Skill. Keep the old executable and configuration until verification finishes; no automatic import of legacy account configuration is promised, so sign in with the new CLI when needed. Do not use legacy installer scripts or reuse legacy submission payloads. For the redesigned standalone 0.3.x series, preserve its existing data directory as described below.
- An `existing-version` result does not authorize replacement. When the user requests an upgrade, preserve a backup of the executable and data before changing anything; never downgrade a newer CLI automatically. For standalone 0.3.x, retain the existing data directory and preserve a private backup if rollback is needed. Finish active local calls and handle pending approvals; the user can stop the old runtime with uppercase `Q` in `tui` before replacing the executable. Lowercase `q` only closes the interface. Stopping the runtime does not cancel platform jobs.
- A Bridge-managed installation follows Bridge's update lifecycle. Do not replace its bundled executable or silently move its account data to a standalone installation.

After an upgrade or move, refresh PATH and verify the actual executable, version, status, and channels. This ClawHub edition resolves the executable locally and does not need embedded Skill reinstallation. New API-key credential files may not be readable by an older CLI, so replacing the executable alone is not a data rollback.
