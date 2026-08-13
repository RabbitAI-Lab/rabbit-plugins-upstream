# Confidence Rules

## Status Meanings

- `confirmed`: supported directly by issuer terms or by multiple approved sources without meaningful disagreement
- `unconfirmed`: plausible and useful, but not fully resolved from approved sources
- `conflicting`: approved sources disagree on a material fact

## Usage

- Prefer `confirmed` whenever issuer documentation is explicit.
- Use `unconfirmed` rather than guessing when a page is vague, stale, or incomplete.
- Use `conflicting` when the answer should preserve disagreement instead of collapsing it.

## Notes

- Every command should include a `confidence_notes` list.
- Keep notes short and tied to a concrete uncertainty.
