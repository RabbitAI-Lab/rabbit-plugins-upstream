---
name: deepwiki
description: "Retrieve source-backed understanding of public GitHub projects: repository structure, package boundaries, architecture, data flow, and codebase-specific behavior. Use for onboarding, subsystem exploration, implementation research, and repository-grounded Q&A when general library documentation is insufficient."
metadata:
  openclaw:
    emoji: "🧭"
    requires:
      bins:
        - bash
        - mcporter
        - jq
        - curl
  related-skills:
    mcporter: to discover and call a configured DeepWiki-capable MCP server.
    context7: for current platform APIs and version-specific product documentation.
---

# DeepWiki Skill

Use DeepWiki to map an unfamiliar public GitHub repository and ask focused questions about its implementation. It provides generated wiki pages and source pointers, not a guarantee of current source or release behavior.

## Workflow

1. **Confirm public visibility.** Normalize an intended-public GitHub URL to `owner/repo` and verify visibility with the unauthenticated GitHub API. Use the canonical `full_name` returned by GitHub rather than the input or a redirected alias. For known private, internal, or unverified targets, do not send their identifiers, code, or metadata to public DeepWiki or a public gateway. Private repositories require a separately authorized Devin MCP integration.
2. **Discover the configured tool family with mcporter.** Use [the workflow reference](references/mcporter-workflow.md) and keep the returned tool names. The official guide still calls the Q&A tool `ask_question`; live schemas may expose `ask_wiki_question`, with a `DeepWiki-` prefix on a gateway. Use the exact name returned by the live schema. Do not change config or initiate OAuth for a lookup.
3. **Start with structure.** Read `read_wiki_structure` and use the topic tree to target the subsystem. If it is sparse, try one narrower question. If it is unavailable or stale, use the public repository sources instead of treating a generated wiki as complete.
4. **Ask a focused question.** Request relevant paths or symbols. Cite useful links returned by DeepWiki; verify claims that would drive a change or depend on a version against the corresponding upstream files or official docs. For a cross-repository question, confirm every repository is public and use an array only if the live schema allows it.
5. **Limit full extraction.** Use `read_wiki_contents` only when the requester explicitly needs the full wiki and smaller queries cannot satisfy the request. Follow [the public MCP fallback](references/api-fallback.md) if no configured route is usable; never switch routes after an authentication or permission error merely to bypass it.

See [tested Bash examples, response shapes, and failure handling](references/mcporter-workflow.md). The official [DeepWiki MCP guide](https://docs.devin.ai/work-with-devin/deepwiki-mcp) covers transport and private repository routing; the [DeepWiki guide](https://docs.devin.ai/work-with-devin/deepwiki) covers generated wikis and Devin-managed steering.
