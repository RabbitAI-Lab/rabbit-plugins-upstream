# Artifact Review

Use this when the user wants to inspect, approve, or reject proposed changes in the TUI. Open Artifact Review with `Ctrl+R`.

1. Move between files with arrow keys.
2. `p` previews one file inline. The preview is truncated.
3. `Enter` opens a full-screen diff.
4. `y` approves. `n` rejects.
5. `A` approves all artifacts in the panel. The current reference does not list `Shift+A` or a bulk-reject key. Older notes used `Shift+A` to approve and `Shift+R` to reject. Recheck `/help` before using those.
6. `Esc` saves state and returns to the prompt.

Code files need an explicit approve or reject. Images and videos sit in a media drawer; `Enter` expands it. Plans, diffs, architecture diagrams, images, and browser recordings can all be artifacts.

## Detail viewer

`Enter` on a row, or the focused `open` button, opens code or markdown.

- `j` / `k` or arrows: line scroll. `PgUp` / `PgDown`: page.
- `g` / `Shift+G`: top / bottom. `l`: line-number gutter.
- `c`: comment on the focused line. `d`: delete that comment.
- `m`: cycle Mermaid modes. `Ctrl+=` / `Ctrl+-`: zoom graphical Mermaid when supported.

Comment before approving a plan or code change.

## Safe defaults

Review generated code before approval in an untrusted repo. Leave `--dangerously-skip-permissions` off when approval matters. Headless work cannot use this panel: ask for the patch summary or commands run. Use a review-requesting policy for multi-file work. `always-proceed` is for trusted, low-risk automation only.
