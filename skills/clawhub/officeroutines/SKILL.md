---
name: officeroutines
description: Read and change Excel, Word, and PowerPoint files from OpenClaw through OfficeRoutines on this computer, including documents open in Office, with undo and replayable recipes.
homepage: https://github.com/recued/office-routines
metadata:
  {
    "openclaw":
      {
        "homepage": "https://github.com/recued/office-routines",
      },
  }
---

# OfficeRoutines

OfficeRoutines gives an agent Excel, Word, and PowerPoint. It changes saved
files through a locked working copy and reads the result back before it
counts, changes documents open in Office as one transaction that is undone if
a step fails, and replays repeated work as saved recipes. It runs on this
computer, and it is built on OfficeCLI.

This skill tells OpenClaw how to work with OfficeRoutines. It installs nothing
and runs no commands.

## Set it up

1. Install OfficeRoutines for your computer from
   https://github.com/recued/office-routines/releases, and install
   [OfficeCLI](https://github.com/iOfficeAI/OfficeCLI#for-humans) too.
2. Add OfficeRoutines to OpenClaw:

   ```
   ofrt job mcp install openclaw
   ```

   When the Office companion is running, this also passes its connection
   file, so OpenClaw can change documents open in Office. Add
   `--allow-folder <folder>` once per folder to limit which saved files
   OpenClaw can open; without it, OpenClaw can open any file your account can.
3. Start a new OpenClaw session, then check it with
   `openclaw mcp probe officeroutines`. It lists 18 tools.

## Working with OfficeRoutines

- OpenClaw shows the tools with the server's name in front, such as
  `officeroutines__officeroutines_help`.
- Start with `officeroutines_help`. It lists the commands and the documents
  open in Office with their pane, each with an alias you can pass as `file`.
- Name a saved file by its full path. Read with `officeroutines_get`,
  `officeroutines_query`, or `officeroutines_view` before you change it.
- `officeroutines_set`, `officeroutines_add`, `officeroutines_remove`, and
  `officeroutines_move` make one change; `officeroutines_batch` makes several
  as one. In a document open in Office, the change appears on screen, and a
  batch that fails partway is undone.
- `save: false` keeps a change on screen for the user to review;
  `officeroutines_save` makes it permanent.
- Give a change a `run_id` when it must happen only once. If the call is cut
  off, `officeroutines_read_batch_run` with the same `run_id` says how it ended;
  do not send the change again before you know.
- For work the user repeats, look for a recipe first:
  `officeroutines_list_recipes`, `officeroutines_read_recipe`, then
  `officeroutines_apply_recipe`. A recipe replays without the model working
  out each step again.
- `officeroutines_copy` copies a file, or makes a PDF of it. It never replaces
  an existing file.
- If OfficeRoutines refuses a path as outside the allowed folders, tell the
  user; only they can change which folders OpenClaw may use.

## Privacy

OfficeRoutines works on files on this computer, and OpenClaw's model sees only
what a tool returns.
