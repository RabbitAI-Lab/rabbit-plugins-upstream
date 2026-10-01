# Publishing Workflow Templates

This module provides templates and conventions for publishing serialized novel content via Git and GitHub. These templates ensure consistent, versioned releases that are easy to track and distribute.

---

## 1. Git Tag Format

### Tag Naming Convention
```
v{major}.{minor}.{patch}
```

### Tag Examples
- `v1.0.0` — Major release (complete arc)
- `v1.1.0` — Minor release (new chapter added)
- `v1.1.1` — Patch release (typo fix, continuity correction)
- `chapter-001` — Chapter-specific tag (optional)

### Tag Message Format
```
v{version}: {brief description}

{detailed description of changes}

Changelog: See CHANGELOG.md
```

---

## 2. Release Note Template

```
# Release [Version] - [Date]

## Summary
[Brief summary of this release]

## What's New
### Chapters
- [Chapter X]: [Brief description]

### Improvements
- [Improvement 1]
- [Improvement 2]

## Fixes
- [Fix 1]
- [Fix 2]

## Known Issues
- [Known issue 1]

## Upgrade Notes
[Any notes for readers upgrading from previous version]

## Full Changelog
See [CHANGELOG.md](CHANGELOG.md) for complete history.
```

---

## 3. Chapter File Naming Convention

### Naming Pattern
```
ch-{chapter_number}-{chapter_title}.md
```

### Examples
- `ch-001-the-beginning.md`
- `ch-042-crossroads.md`
- `ch-100-finale.md`

### Frontmatter Requirements
Every chapter file MUST include YAML frontmatter:

```yaml
---
chapter: {number}
title: "{chapter title}"
pov: {POV character name}
date: YYYY-MM-DD
word_count: {approximate word count}
status: draft|review|published
license: CC-BY-NC-SA-4.0
---
```

**File-header order.** Two rules both claim the top of a chapter file: the YAML frontmatter
above, and spec Section 0.5's requirement that every generated novel file *begin* with the
CC BY-NC-SA 4.0 header block. They are reconciled as follows, and every chapter file uses
this exact order:

1. **YAML frontmatter first, at byte 0** — any content before the opening `---` stops tools
   from parsing it as frontmatter. The `license:` key here is the machine-readable licence
   declaration that the release workflow's licence gate checks.
2. **CC BY-NC-SA 4.0 header block second** — the human-readable block from spec Section 4.3,
   before any narrative prose.

See [example-chapter-draft.md](examples/example-chapter-draft.md) for a worked instance.

### File Structure
```
chapters/
├── ch-001-the-beginning.md
├── ch-002-first-steps.md
├── ch-003-the-call.md
└── ...
```

---

## 4. Publishing Checklist

```
# Publishing Checklist

## Pre-Publish Verification
- [ ] Continuity check passed (see method-patterns-continuity.md)
- [ ] Chapter formatting verified
- [ ] License headers present
- [ ] Word count documented
- [ ] POV character documented
- [ ] Timeline consistency verified
- [ ] Character states updated
- [ ] Unresolved threads logged

## Git Operations
- [ ] All changes committed with descriptive message
- [ ] CHANGELOG.md updated
- [ ] Tag created with proper format
- [ ] Tag message follows convention

## Post-Publish
- [ ] Release notes published
- [ ] Readers notified (if applicable)
- [ ] State files updated
- [ ] Feedback collected
```

---

## 5. Version Bumping Guide

### When to Bump
| Change Type | Version Bump | Example |
|-------------|-------------|---------|
| Major release (complete arc) | MAJOR | v1.0.0 → v2.0.0 |
| New chapter/content added | MINOR | v1.1.0 → v1.2.0 |
| Typo/continuity fix | PATCH | v1.1.1 → v1.1.2 |

### Bumping Process
1. Update version number in relevant files
2. Update CHANGELOG.md with release notes
3. Commit changes: `git commit -m "chore: bump version to vX.Y.Z"`
4. Create tag: `git tag -a vX.Y.Z -m "vX.Y.Z: {description}"`
5. Push to remote: `git push origin vX.Y.Z`

---

## 6. GitHub Release Workflow

### Automated Release Steps
1. **Validate**: Check file formats and naming conventions
2. **Verify**: Run continuity checks and license compliance
3. **Package**: Prepare release assets
4. **Publish**: Create GitHub Release with notes
5. **Notify**: Update readers/community

### Manual Release Steps
1. Ensure all checklist items are complete
2. Update CHANGELOG.md
3. Commit and tag with proper version
4. Push to remote
5. Create GitHub Release with release notes

---

## Cross-References

- See [method-patterns-worldbuilding.md](method-patterns-worldbuilding.md) for world-building elements.
- See [method-patterns-character.md](method-patterns-character.md) for character design templates.
- See [method-patterns-chapter.md](method-patterns-chapter.md) for chapter writing templates.
- See [method-patterns-continuity.md](method-patterns-continuity.md) for continuity tracking templates.

---

## License

Licensed under GNU General Public License v3.0 (GPL-3.0). Generated novel content produced using these templates is licensed under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
