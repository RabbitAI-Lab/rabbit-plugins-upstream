# Changelog

All notable changes to this skill are documented here.
Format loosely follows [Keep a Changelog](https://keepachangelog.com/); versions follow [SemVer](https://semver.org/).

### v1.2.2 (2026-07-31)

- Fixed: Support both UI entry points (top tab + dropdown menu) with automatic fallback
- Fixed: Correct v1.2.0 changelog — both methods are valid, not a UI deprecation

### v1.2.1 (2026-07-31)

- Fixed: Frontmatter dependency declaration for skill-release-audit
  - Add `bins: [ego-browser, node]`
  - Move env vars to `metadata.openclaw.requires.env`

### v1.2.0 (2026-07-31)

- Fixed: Add top "上传图文" tab as alternative entry point (both tab and dropdown work)
- Fixed: Update publish success verification to also recognize `published=true` URL parameter
- Fixed: Increase post-upload wait to 10s for more reliable image processing

### v1.1.0 (2026-07-31)

- Added formal Dependencies section with ego-browser install/verification instructions
- Fixed shell injection risk in publish_note.sh (params now passed via process.env)
- Strengthened guardrail statements for high-risk operations ("不要" → "严禁")
- Added TITLE/BODY special character restrictions
- Fixed file path references in Resources section (added scripts/ and references/ prefixes)
- Added `set -euo pipefail` to publish_note.sh
- Updated Repository URL to better-office-work-flow monorepo
- Passed skill-release-audit 6/6 modules (0 WARN, 0 ERR)
- Passed UGLIC check + skill-deep-audit (107/115, PASS)

### v1.0.0 (2026-07-31)

- Initial open-source release
