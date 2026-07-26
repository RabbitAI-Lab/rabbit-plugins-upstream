# Changelog

## [1.2.4] - 2026-07-22

### Fixed
- Fixed duplicate writes to the daily briefing file under certain race conditions (#42)
- Fixed missing retry when the OpenWeatherMap API returns a 503
- Moved the API key out of the logged request URL entirely (see Security below and `SECURITY.md`)

### Security
- Fixes the credential-leak issue disclosed in 1.2.3. Users on 1.2.3 or
  earlier should upgrade and rotate their `OPENWEATHER_API_KEY`.

## [1.2.3] - 2026-07-15 · HIDDEN

### Security
- ⚠️ Hidden from ClawHub on 2026-07-16 (`clawhub skill hide`). Under a
  specific API-timeout retry path, this version could write the raw
  `OPENWEATHER_API_KEY` into local debug logs.
- Affected users: upgrade to 1.2.4 and rotate `OPENWEATHER_API_KEY`.
- Full incident timeline: see `SECURITY.md`.

## [1.2.0] - 2026-07-10

### Added
- Support for a custom daily-briefing template path (see README)

### Changed
- Default output location changed to `~/Obsidian/Daily/` to match most
  users' setup

## [1.1.0] - 2026-07-01

### Added
- Support for querying a different city per run via the skill's input

## [1.0.0] - 2026-06-20

### Added
- First stable release: single-city daily weather briefing written to
  Obsidian

## [0.1.0] - 2026-06-15

### Added
- Initial release for internal testing
