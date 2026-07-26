# Install

## Package Contents

- Binary: `assets/bin/skillscan`
- Skill document: `SKILL.md`
- Build metadata: `assets/build/build-info.json`
- SHA-256: `assets/build/skillscan.sha256`

## Install Steps

1. Unzip the release package.
2. Optionally verify the checksum:

```bash
shasum -a 256 assets/bin/skillscan
cat assets/build/skillscan.sha256
```

3. Run the binary directly:

```bash
./assets/bin/skillscan review /path/to/skill
./assets/bin/skillscan review /path/to/skills --output-dir /tmp/skillscan-out
```

The default engine is `auto`: it prefers a locally resolved external scanner and falls back to the built-in native engine if the external scanner is unavailable or fails. Use `--engine native` to run only the built-in engine.

4. If you want to require an external scanner bridge:

```bash
./assets/bin/skillscan review /path/to/skill --engine external
```

5. To opt into LLM semantic review, configure a trusted OpenAI-compatible endpoint. `native`, `external`, and `auto` all support `--use-llm`; external scanners must support the Cisco-compatible `--use-llm` contract.

```bash
./assets/bin/skillscan review /path/to/skill --engine native --use-llm \
  --llm-endpoint http://localhost:11434/v1 \
  --llm-model your-model
```

With `native`, this sends a bounded, basically redacted text packet from the target package to that endpoint. If the LLM is unavailable, the native static result still returns and records `engine.fallback_reason`.

For `external`, CMIC adds `--use-llm` and passes the endpoint, model, and optional key through
`SKILL_SCANNER_LLM_BASE_URL`, `SKILL_SCANNER_LLM_MODEL`, and `SKILL_SCANNER_LLM_API_KEY` only to the child
process. The external scanner controls its own data packet and failure handling; `auto` falls back to native if
the external process fails.

6. For batch review in enterprise environments:

```bash
./assets/bin/skillscan review /path/to/skills \
  --output-dir /tmp/skillscan-out \
  --upload-url https://scanner.example.com/api/report \
  --instance-id prod-a1
```

The upload payload contains embedded review details for each skill, including the full scan summary and findings.

## Common Commands

```bash
./assets/bin/skillscan inspect /path/to/skill
./assets/bin/skillscan scan /path/to/skill
./assets/bin/skillscan review /path/to/skill
./assets/bin/skillscan benchmark --engine native
./assets/bin/skillscan package-skill
```
