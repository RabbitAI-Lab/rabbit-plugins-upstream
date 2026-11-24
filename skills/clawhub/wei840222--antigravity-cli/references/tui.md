# Interactive TUI

Launch `agy` in the project directory. Type `/` for typeahead.

Commands and keybindings: `references/command-reference.md`. Custom bindings and prompt tips: `references/settings-and-tips.md`.

## Composition

- `Enter` submits.
- `Shift+Enter`, `Ctrl+J`, or `Alt/Option+Enter` inserts a newline.
- A trailing `\` plus `Enter` inserts a newline in any terminal.
- `Ctrl+G` on an empty prompt opens `$EDITOR`. Save and exit to import the draft.
- `Esc` stops a turn, command, or search that is going wrong.
- `@` inserts a full path. A leading `!` runs a shell command. `?` lists slash commands.
- `Esc Esc` clears the box when nothing is streaming.
- Set verbosity to `low` in `/config` when tool output is noisy.

## Media

`Ctrl+V` or native paste accepts clipboard media. Formats: PNG, JPEG, GIF, WebP, BMP, TIFF, SVG, MP4, MOV, WebM, AVI.

## Steering

`/rewind` or `/undo` returns to an earlier message. `/fork` branches an experiment; the workspace stays. `/resume` switches threads. `/agents` monitors background subagents. `Ctrl+K` approves the pending subagent action in the status alert.
