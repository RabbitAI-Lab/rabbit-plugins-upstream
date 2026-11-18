# skill-audit

**The autonomous auditor for the agent-skills economy.** An agent that discovers skills in any repo or marketplace, flags prompt-injection and security risks, scores quality and publishes a public leaderboard. Static analysis only — nothing gets executed. Zero dependencies, Node >= 18.

## Quickstart (the agent)

    git clone https://github.com/hugororo2003/skill-audit && cd skill-audit
    cp config.example.json config.json
    node agent.js --top 20 --no-publish     # audits anthropics/skills + addyosmani/agent-skills

Output in `public/`: per-skill HTML report cards (`public/cards/`) + `leaderboard.html` + `leaderboard.json`, sorted by score.

## What it audits
- **Safety (critical, caps score at 25 → F)**: instruction override attempts, system prompt extraction, remote exfiltration endpoints, unverified shell execution pipelines, dynamic code evaluation, hidden unicode or zero-width obfuscation, hardcoded credentials or private keys, and destructive filesystem modifications.
- **Structure**: frontmatter, name, description quality, usage & procedure sections.
- **Clarity / maintainability**: vague specs, size, license.

Grades A ≥ 90 · B ≥ 75 · C ≥ 60 · D ≥ 45 · F below. Any critical finding caps the score at 25.

## Run it yourself (CLI / CI)

    node bin/cli.js ./some-skill --out reports/

Or run directly from GitHub without installing:

    npx github:hugororo2003/skill-audit ./some-skill --out reports/

Exit code 1 on critical findings — use it as a PR gate for your own skills repo.

## Autonomous publishing
Set `GITHUB_TOKEN` + `PUBLISH_REPO`, `publish: true` in config → the agent pushes leaderboard + cards to the `gh-pages` branch on every run. `--watch 60` keeps it looping. Optional Telegram notifications (`TG_BOT_TOKEN`, `TG_CHAT_ID`).

## Also a skill
Install this repo as a skill and your own agent audits third-party skills before installing them (`SKILL.md`).

## Why
Skill marketplaces are exploding (anthropics/skills: 195k⭐) with zero quality control. Prompt-injection via SKILL.md is the vulnerability nobody is watching. skill-audit is the missing gate — and its leaderboard is public infrastructure.

## Author & License
Created and maintained by Hugo Rodriguez ([@hugororo2003](https://github.com/hugororo2003)). Released under the MIT License.
