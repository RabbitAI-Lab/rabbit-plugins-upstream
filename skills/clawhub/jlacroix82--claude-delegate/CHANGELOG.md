# Changelog

All notable changes to this skill.

## [Unreleased]

### Added
- Initial release of claude-delegate skill
- Wrapper script for Claude Code print mode (`claude -p`)
- Permission level mapping (read-only -> plan, workspace-write -> acceptEdits, danger-full-access -> bypassPermissions)
- Direct `--permission-mode` override
- stream-json event logging with final-answer extraction
- Piped stdin support for test output and other context
- Prompt file and stdin-file support
- Tool allowlist (`--allowed-tools`) and model selection (`--model`)
- Enterprise-friendly: uses saved OAuth login, no API key required
- Comprehensive safety rules (no API key passthrough, no credentials.json access)
