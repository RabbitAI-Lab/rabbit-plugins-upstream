# Dongwo（懂我）

A zero-service, Markdown-based preference memory shared by coding agents.

Dongwo uses lifecycle hooks plus a small Python standard-library engine to:

- capture preference-like prompts into separate per-agent inboxes;
- skip ordinary prompts and prompts matching common sensitive-data rules;
- distinguish explicit preferences, stable observations, and unresolved items;
- rebuild an auditable Markdown memory;
- inject a short context snapshot into Codex and Claude Code.

## Install

```bash
clawhub install @cutd/dongwo
cd skills/dongwo
python3 scripts/setup.py --root /path/to/project
python3 scripts/setup.py --root /path/to/project --apply
```

The first setup command previews changes. `--apply` installs the engine under
`.dongwo/` and prints configuration snippets. It deliberately does not
overwrite existing Codex or Claude Code configuration.

If a different engine already exists at the target path, setup stops before
printing runnable hook snippets. Review the conflict and use `--force` only when
you want to replace it with the bundled, hash-verified engine.

`myprofile.md` is not trusted merely because it contains marker comments. After
reviewing the complete profile, explicitly bind trust to its current digest:

```bash
python3 .dongwo/scripts/dongwo.py profile trust
python3 .dongwo/scripts/dongwo.py profile trust --apply
```

The trust record is stored outside the project in a user-level Dongwo config
directory. Any later edit invalidates trust and the profile is omitted from
injected context until approved again.

Inbox evidence is also authenticated with trust state stored outside the
project. New hook-captured events are registered automatically. Existing
unsigned events remain on disk but require review and `inbox trust --apply`
before they can contribute to generated context; edits invalidate their hashes.

## Privacy

The published package contains only code and documentation. It does **not**
contain the author's profile, prompt inbox, generated context, or personal
memory.

Keep these local and private:

- `myprofile.md`
- `.dongwo/memory/`
- legacy `03_Projects/15_懂我/memory/`

Preference evidence is retained locally until removed. Review the inbox before
using Dongwo for confidential work. To forget an item, delete the matching
inbox evidence after explicit confirmation and run `consolidate`.

## Requirements

- Python 3.10+
- macOS or Linux (`fcntl` file locking)
- a client that supports lifecycle command hooks for automatic capture/injection

## License

Skills published on ClawHub use the registry's default MIT-0 license.
