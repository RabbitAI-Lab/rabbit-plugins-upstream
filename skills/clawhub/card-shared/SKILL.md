---
name: card-shared
description: Shared research policy and output contracts for the card command suite (card-full, card-transfer, card-rate, card-news, card-credits, card-compare, card-value, card-wallet, and card-profile-recommend). Use as background reference, not as a user-facing command.
---

# Card Shared

## Purpose

This hidden skill holds the shared rules for the card command suite. User-facing commands should reuse these files instead of redefining sourcing, confidence, or output contracts independently.

## Shared References

- [source-policy.yaml](source-policy.yaml) for issuer-first research, approved secondary sources, issuer blog/newsroom policy, the fast-search policy, and URL fetch-safety rules
- [command-contracts.yaml](command-contracts.yaml) for required sections and YAML keys
- [section-definitions.md](section-definitions.md) for `/card-full` composition rules
- [../card-identity/SKILL.md](../card-identity/SKILL.md) for centralized card-name resolution, abbreviation handling, and disambiguation
- [card-identity-rules.md](card-identity-rules.md) for card matching and ambiguity handling rules
- [confidence-rules.md](confidence-rules.md) for `confirmed`, `unconfirmed`, and `conflicting`
- [recency-rules.md](recency-rules.md) for freshness expectations, especially `/card-news`
- [normalization-rules.md](normalization-rules.md) for shared formatting and field conventions

## Shared Behavior

1. Identify the exact card variant first. If ambiguous, return a numbered choice list and stop.
2. Follow the fast-search policy: use one shared discovery pass, issuer pages first, and stop once the contract is satisfied. Treat secondary research and offer history as exception paths, not defaults.
3. Fetch result pages with `WebFetch` only after they pass the shared host allowlist and URL-safety rules in `source-policy.yaml`.
4. Mark uncertain or conflicting claims explicitly in `confidence_notes`.
5. Return compact markdown with emoji section headings and numbered lists.
6. Keep `sources` in the hidden YAML block only — do not show a visible sources footer.
7. YAML is internal only — never include it in user-facing output.
8. Omit the Card Identity section when the match is confident.

## Composition Note

`/card-full` composes from `/card-rate`, `/card-transfer`, and `/card-credits`. `/card-news` is intentionally independent — news is time-windowed and conceptually separate from the static card framework. `/card-compare`, `/card-value`, and `/card-wallet` are multi-card or analytical commands that reuse the same shared rules but have their own contracts.
