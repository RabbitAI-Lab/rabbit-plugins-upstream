---
name: deepwiki
description: "Retrieve source-backed understanding of public GitHub projects: repository structure, package boundaries, architecture, data flow, and codebase-specific behavior. Use for onboarding, subsystem exploration, implementation research, and repository-grounded Q&A when general library documentation is insufficient."
metadata:
  openclaw:
    emoji: "🧭"
    requires:
      bins:
        - mcporter
        - jq
        - curl
  related-skills:
    mcporter: to discover and call a configured DeepWiki-capable MCP server.
    context7: for current official library, framework, SDK, API, and version-specific documentation beyond one repository's implementation.
---

# DeepWiki Skill

Use this skill when the task needs a high-level understanding of a public GitHub repository, generated architecture documentation, source-linked wiki pages, or repository-grounded Q&A.

## Core Rule

Use the `mcporter` skill to discover a configured server exposing all three DeepWiki tools. Do not assume a gateway name, URL, or authentication arrangement. Do not use native DeepWiki tool wrapper syntax from this skill.

## Tool Choice

1. Use `DeepWiki-read_wiki_structure` first to inspect available wiki topics for a repository.
2. Use `DeepWiki-ask_question` for focused repository questions and architectural explanations.
3. Use `DeepWiki-read_wiki_contents` only when the full generated wiki is needed; it can return very large output.

## Decision Checkpoints

1. **🔴 CHECKPOINT — Repository visibility:** Run the repeatable Visibility Preflight in `references/mcporter-workflow.md` before a public DeepWiki call and assign its stdout to `repo_name`. Proceed only when it returns a canonical public `owner/repo`; use that returned value for every subsequent DeepWiki call. Private or unverified repositories stop here; do not send their name, URL, source, or metadata to public DeepWiki.
2. **🔴 CHECKPOINT — Structure quality:** After `read_wiki_structure`, confirm the response contains usable topics for the requested subsystem. If it is empty or sparse, follow the Failure Matrix instead of treating generated wiki output as complete.
3. **🔴 CHECKPOINT — Full-content budget:** Before `read_wiki_contents`, confirm that the user explicitly needs broad extraction, audit, or offline use and that focused questions cannot satisfy the request. If the user did not explicitly request full contents, ask before making this large-output call.

## Quick Commands

```bash
# Run the bounded Server Discovery procedure in
# references/mcporter-workflow.md and assign its stdout to $deepwiki_server.

mcporter call "$deepwiki_server.DeepWiki-read_wiki_structure" \
  --args "$(jq -nc --arg repo "$repo_name" '{repoName: $repo}')" \
  --output json

mcporter call "$deepwiki_server.DeepWiki-ask_question" \
  --args "$(jq -nc --arg repo "$repo_name" --arg question "What is the high level architecture?" '{repoName: $repo, question: $question}')" \
  --output json

mcporter call "$deepwiki_server.DeepWiki-read_wiki_contents" \
  --args "$(jq -nc --arg repo "$repo_name" '{repoName: $repo}')" \
  --output json
```

## Workflow

1. Normalize repository names to `owner/repo` and pass the Repository visibility checkpoint.
2. Run the bounded server discovery in `references/mcporter-workflow.md`; use its selected server for all calls in this task.
3. If no configured DeepWiki-capable server is available, use the direct public MCP fallback only for a confirmed public repository.
4. Read wiki structure and pass the Structure quality checkpoint.
5. Prefer `ask_question` for targeted answers.
6. Pass the Full-content budget checkpoint before using full wiki contents for broad summaries, audits, or offline extraction.
7. Report DeepWiki source links or source-file references when grounding matters.

## Coverage and Limits

- Public DeepWiki and DeepWiki MCP provide basic documentation and Q&A for public GitHub repositories.
- Private repository capabilities require a Devin account and the Devin MCP server with a Devin API key.
- DeepWiki generated docs are useful for onboarding, architecture discovery, and repository exploration; verify critical implementation claims against source files when risk is high.
- `.devin/wiki.json` can steer wiki generation in Devin-managed repositories, but creating or changing it is a repository edit and should follow normal repo workflow.

## Detailed References

Use `references/mcporter-workflow.md` for command patterns, field shapes, query design, and source-backed answer patterns.

Use `references/api-fallback.md` only after configured-server discovery finds no compatible server, when validating a direct DeepWiki MCP integration, or when the task specifically asks about API access. Never use the public fallback for private or unverified repositories.

## Anti-Patterns

| Do not | Why | Correct action |
| --- | --- | --- |
| Skip the Visibility Preflight or treat an unknown repository as public | A private repository name or metadata may be sent to public DeepWiki. | Stop unless the preflight returns a canonical public `owner/repo`; use an approved Devin MCP path for private repositories. |
| Verify a redirected repository but query DeepWiki with the original name | The verified GitHub target and the queried repository can diverge. | Use only the canonical `full_name` emitted by Visibility Preflight for all subsequent `repoName` values. |
| Hardcode a gateway or server alias | Another runtime may use a different server name or no gateway at all. | Use bounded capability discovery and keep the selected `deepwiki_server` for the task. |
| Call `read_wiki_contents` before reading structure | It can create needless large output and hides the useful topic map. | Start with `read_wiki_structure`, then ask one focused question per subsystem. |
| Retry timeouts, rate limits, or auth failures without a bound | Repeated requests can amplify load, duplicate data exposure, or conceal a broken integration. | Follow the Failure Matrix: bounded candidate failover, one rate-limit retry, then stop or use source fallback. |
| Treat generated wiki output as sufficient evidence for consequential code or security decisions | Generated pages can be sparse, stale, or omit implementation details. | Verify consequential claims against repository source before editing or recommending a change. |
| Send private repository data to public DeepWiki or direct public MCP | Public DeepWiki is not the approved private-repository path. | Require explicit approval of a Devin account, private MCP integration, permissions, and transport path. |

## Official Documents

These are the official documents this skill was built from:

- `https://deepwiki.com/`
- `https://docs.devin.ai/work-with-devin/deepwiki`
- `https://docs.devin.ai/work-with-devin/deepwiki-mcp`
