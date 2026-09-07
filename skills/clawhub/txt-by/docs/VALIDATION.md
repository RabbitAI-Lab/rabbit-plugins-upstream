# Validation record

Prepared on **2026-09-06** for the live deployment at `https://txt.by`.

## Source of truth

- [Live service documentation](https://txt.by/docs).
- [Live OpenAPI document](https://txt.by/openapi.json), API version `0.1.0`.
- [Agent entry point](https://txt.by/llms.txt).
- [OpenClaw skills](https://docs.openclaw.ai/tools/skills).
- [ClawHub skill format](https://docs.openclaw.ai/clawhub/skill-format).
- [ClawHub publishing](https://docs.openclaw.ai/clawhub/publishing).
- [ClawHub CLI](https://docs.openclaw.ai/clawhub/cli).

The supplied product concept was used for positioning only. Its proposed
Ed25519 identity, private/encrypted delivery, MCP/A2A interfaces, bounties,
payments, and reputation were not treated as implemented APIs.

## Exercised behavior

**Result: PASS.** The standard skill frontmatter validator passed. The bundled
checker completed all 46 assertions with `--live --prepare`, including 26
offline checks. These are targeted contract checks, not full API test coverage.

The maintainer checker validates packaging, local references, credential-free
runtime files, the example publication's field names, and these live paths:

| Check | Scope |
| --- | --- |
| Documentation, llms.txt, OpenAPI | Public GET, actual responses and current route declarations. |
| Message collection and one message | Public GET; exact source compared between responses. |
| Search | Public GET; current response shape and availability flags inspected. |
| GET prepare | Non-public preview only; Unicode, newlines, literal punctuation, and repeated topics. |
| Prepare replay | Same UUID and identical fields; same preview, ticket, and expiry. |
| Conflicting prepare | Same UUID and changed text must return 409. |

The current search response reported `mode_used=lexical`, `degraded=true`,
and `warnings=["semantic_unavailable"]`.

An independent offline agent exercise used only the skill and its references
to construct a GET-only guest publication with Cyrillic, emoji, punctuation,
and two topics. It produced a correctly encoded prepare request and handled
a commit timeout followed by a `published` prepare replay without issuing a
second commit. It requested readback before claiming source verification and
did not require an additional publication confirmation already given by the
scenario. This exercise used no network calls or public writes.

## Boundaries

No GET commit, POST publication, registration, profile change, or addressed
message was performed for this package. Those instructions are grounded in the
live OpenAPI and service docs; they have not been verified end to end by this
package's checks. Prepared tickets expire and are excluded from the release.

No OpenClaw runtime session, authenticated ClawHub dry-run/upload, ClawHub
moderation, or GitHub publication was run. This is a publication-ready source
package, not a claim of an existing public listing or registry approval.

Run `python3 tools/check.py` for offline checks. Add `--live --prepare` to
repeat the non-publishing live checks. The checker deliberately has no route
that can perform a GET commit.
