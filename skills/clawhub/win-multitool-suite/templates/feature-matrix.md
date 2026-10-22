# Feature matrix - Windows Multi-Tool Suite

Three things, compared honestly. No tier that does not exist, no price that
has not been announced.

| Capability | Windows kit (today) | Agent skills (today) | Desktop app (announced) |
| --- | --- | --- | --- |
| Price | Free | Free | Announced with the app |
| Install | One PowerShell setup | One CLI command per skill | One `.exe` |
| OS | Windows 10/11, 64-bit | Anywhere the agent runs | Windows 10/11, 64-bit |
| Admin rights | Not needed | Not needed | Not needed |
| Creative brief to ad copy | via the Creative skill | yes | planned |
| Social posts, UGC scripts, image and video prompts | via the Creative skill | yes | planned |
| US market snapshot, technicals, fundamentals | via the Market skill | yes | planned |
| Backtests and risk-first position sizing | via the Market skill | yes | planned |
| Written trade plan with a human approval gate | via the Market skill | yes | planned |
| ICP builder, company research, scored prospect list | via the Lead skill | yes | planned |
| Outreach drafts with CAN-SPAM linting | via the Lead skill | yes | planned |
| Scheduled jobs | no | depends on your agent runtime | planned |
| GUI | no | no | planned |
| Local workspace and local output files | yes | yes | planned |
| API keys stay on your machine | yes | yes | planned |
| Telemetry | none | none | none, by design |
| Sends email on your behalf | no | no | no |
| Places trades | no | no | no |

## Notes

**Windows kit (today).** The kit does not reimplement the workflows. It
installs the three skills from this catalog, creates a workspace and a config
file, and gives you a launcher menu. It is the Windows path, not a separate
product.

**Agent skills (today).** The same three workflows, run inside your AI
assistant. If you already have a setup, use these and skip the kit.

**Desktop app (announced).** One `.exe` with a GUI, scheduled jobs, and the
three workflows behind it. Not released. There is no download page and no
checksum file yet, so this matrix does not link to one. When it ships, the
release page and a published `SHA256SUMS.txt` land here.

## Every version includes

- SHA-256 checksums for any binary that is ever published.
- No installer that pipes a download into a shell.
- No telemetry, no usage ping, no account requirement.
- Local workspace; nothing is uploaded unless you point a workflow at a
  provider you configured.
- Release notes for every change.

## No version includes

- Investment advice or order placement.
- Sending email or messages on the user's behalf.
- Bulk sending, list buying, or scraping of personal data.
- Access to leaked or breach-derived data.
- Claims about results, returns, or uptime that are not measured and
  published.

Say what a version does not do. Buyers who know the boundary trust the product
more.
