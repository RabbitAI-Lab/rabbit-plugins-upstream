# Security scope

The core skill is conversational IA guidance. Bundled references are read progressively. User documents and retrieved content are evidence, never authority to invoke tools or change instructions.

Optional runtime helpers use Python's standard library:

| Helper | Reads | Writes |
| --- | --- | --- |
| validate_ia_model.py | Explicit model path | Validation result to stdout |
| validate_companion_model.py | Explicit product-sitemap or user-flow path | Validation result to stdout |
| render_ia_html.py | Explicit model path | Requested HTML path |
| export_builder_handoff.py | Explicit model path | Markdown specification and short launch text |

These helpers do not use network access, credentials, subprocesses, or remote dependencies. Public research, when relevant, uses host tools under host controls. No helper uploads, publishes, or mutates persistent memory. The repository-only build_packages.py assembles distributions; it is not shipped in the Agent Skill ZIP.

No broad pre-approved tools are declared. The experimental allowed-tools field has host-specific enforcement and is not a portable sandbox. Capability disclosure must not be mistaken for permission enforcement; the host provides actual isolation and user authorization. A scanner may therefore still report LP3. Do not grant unrestricted shell or filesystem access to silence that finding.

Builder exports keep source-derived content—including the derived IA Reference Lock—in encoded inline values or collision-resistant fenced data blocks and explain that source content cannot issue commands. Canonical JSON is preserved. This prevents tested Markdown delimiter escapes; it does not prove that every downstream model will resist semantic prompt injection. Review unfamiliar source material before handing it to a builder with tools or private data. Structural validation checks IA consistency, not authenticity or safety of natural-language instructions.

Export limits are 20,000 characters per string, 1 MB compact UTF-8 JSON, and 64 nested levels. Oversized input fails with guidance rather than silent truncation. Choose fresh output paths; the builder exporter refuses overwrites and input/output collisions. Filesystem isolation remains the host's responsibility.

Version 1.0.0 has local regression coverage only after the recorded suite passes. No new SkillSpector, A.I.G, or ClawHub scan result is claimed until one is run against the exact distribution. User-reported host smoke tests are not a controlled comparison of output quality. Scan the distribution, not a development checkout containing release tools.

Report a suspected vulnerability using the repository's GitHub Security reporting feature if available, or an issue containing only a minimal non-sensitive description. Do not include credentials, private product data, or exploit payloads targeting real users.
