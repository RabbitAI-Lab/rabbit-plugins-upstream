# Bounty Hunting Examples

## Real-World Bounty Scans

### Session: May 14, 2026
**Search Queries Used:**
- `gh search issues --label "💎 Bounty" --state open --sort created --limit 20 --json repository,title,url,labels,createdAt`
- `gh search issues --label "bounty" --state open --sort created --limit 20 --json repository,title,url,labels,createdAt`
- `gh search issues --repo openai/openai-python --label "good first issue" --state open --sort created --limit 10 --json repository,title,url,labels,createdAt`
- `gh search issues --repo openai/openai-python --label "enhancement" --state open --sort created --limit 10 --json repository,title,url,labels,createdAt`

### Key Findings

#### High-Value Bounties (Meeting Criteria)
**None found** - No USD bounties $50+ in last 48 hours with target languages

---

### Session: May 17, 2026
**Search Queries Used:**
- Same as May 14 session (standard 4-query pattern)
- Additional: `gh repo view OWNER/REPO --json languages` for language verification
- Additional: `gh search prs --repo OWNER/REPO --state open --limit 10 --json title,url,createdAt` for competition check

### Key Findings

#### High-Value Bounties Found
**ClankerNation/OpenAgents** — 15+ Python/Solidity/TypeScript bounties ($2k–$9k)
- Suspicious: mass-created in 2 minutes, "Autonomous Agents Only" label
- Python API issues most accessible: #187 ($7k), #188 ($7k), #192 ($3k), #197 ($2k), #200 ($2k)
- Competition: Medium (10+ PRs on other issues in the repo)

**UnsafeLabs/RFC-5322 #1** — $400 ABNF email parser
- Fresh repo, zero competition
- Language not yet determined (empty languages field)

**SecureBananaLabs/bug-bounty** — $350–$750 JS/TS bounties
- #30 ($750 API benchmark): 5+ PRs within 6 hours — EXTREME competition
- #29 ($500 Admin Panel): 3+ PRs — HIGH competition

**tenstorrent/tt-metal #44507** — $3k exp2 optimization (C++/Python)
- 1 competing PR (#44567)
- Hardware-specific knowledge required

#### openai-python Issues
- #3201 (streaming tool_call deltas): 4 competing PRs already (#3241, #3245, #3246, #3247) — race lost
- #3180 (default web search to approximate): OPEN, zero comments, no PRs — good opportunity
- #3224 (empty api_key breaking change): PR #3242 already exists
- #3231 (reasoning summary on codex): API-side issue, not fixable via SDK PR

#### PR Status
- openai-python #3194 (shell completion): OPEN, MERGEABLE, REVIEW_REQUIRED
- openai-python #3180: This is an ISSUE, not a PR (user confusion — always verify)

#### Lessons from This Session
1. **ClankerNation/OpenAgents pattern**: Mass-created "Autonomous Agents Only" bounties are a new farm pattern. Verify payout before investing.
2. **openai-python #3201 race**: 4 competing PRs accumulated in 2 days. For high-profile bugs, speed matters — check PRs BEFORE writing code.
3. **Issue vs PR**: User tracked "#3180" as a PR but it was an issue. Always `gh pr view` first, fall back to `gh issue view`.

#### Recent Low-Value Bounties
**UnsafeLabs/Bounty-Hunters** (JavaScript)
- Issues #409, #408, #393, #392, #391, #390, #389
- Created: May 13-14, 2026
- Amount: $1 each
- Language: JavaScript ✓
- Competition: Low (no PRs found)

#### Point-Based Bounties
**waxeye7/screeps-bounty-arena** (JavaScript)
- Issues #57, #56, #43 (created May 13-14)
- Language: JavaScript ✓
- Value: 1-5 points (no USD conversion)
- Competition: Medium (some have "status:has-pr" labels)

#### OpenAI Python Opportunities
**Good First Issues:**
- #843: Shell auto completion (Nov 17, 2023)
- #622: Chat Fine-Tuning CLI (Sep 21, 2023)

**Recent Enhancements:**
- #2404: Retry logging (Jun 10, 2025)
- #2093: Structured Outputs BaseModel (Feb 5, 2025)

### Competition Analysis Examples

#### Extreme Competition
**Memanto + LangGraph Bounty ($100)**
- Repository: moorcheh-ai/memanto
- Created: May 11, 2026
- PR Count: 20+ open PRs
- Competition Level: EXTREME
- Score: 0/10 (despite high value)

#### Low Competition  
**UnsafeLabs Bounty-Hunters ($1)**
- Repository: UnsafeLabs/Bounty-Hunters
- Created: May 13-14, 2026
- PR Count: 0
- Competition Level: LOW
- Score: 4/10 (low value but accessible)

### Authentication Patterns

#### Successful Authentication
```bash
# Initial check
gh auth status
# Output: ✓ Logged in to github.com account lrg913427-dot

# Search execution
gh search issues --label "💎 Bounty" --state open --sort created --limit 20 --json repository,title,url,labels,createdAt
# Success: Returns JSON data
```

#### Authentication Troubleshooting
```bash
# Problem: GH_TOKEN environment variable conflict
gh auth status
# Output: X Failed to log in to github.com using token (GH_TOKEN)

# Solution: Clear environment token
unset GH_TOKEN
gh auth status
# Output: ✓ Logged in to github.com account lrg913427-dot
```

### JSON Parsing Examples

#### Bounty Issue JSON Structure
```json
{
  "createdAt": "2026-05-13T20:04:40Z",
  "labels": [
    {"name": "💎 Bounty"},
    {"name": "$1"},
    {"name": "good first issue"},
    {"name": "help wanted"}
  ],
  "repository": {
    "name": "Bounty-Hunters",
    "nameWithOwner": "UnsafeLabs/Bounty-Hunters"
  },
  "title": "[ Javascript ] Fix cross-file dependency cycle...",
  "url": "https://github.com/UnsafeLabs/Bounty-Hunters/issues/409"
}
```

#### PR List JSON Structure
```json
{
  "number": 478,
  "title": "fix: [BOUNTY $100] 🐜 The Memanto + LangGraph Integration Challenge...",
  "author": "utkarsh3010-maker",
  "state": "OPEN",
  "createdAt": "2026-05-14T00:11:48Z"
}
```

### Evaluation Scenarios

#### Scenario 1: High-Value but High Competition
- **Issue**: Memanto $100 bounty
- **Value**: $100 (3 points)
- **Language**: Python (2 points)  
- **Competition**: Extreme (0 points)
- **Freshness**: 3 days old (0 points)
- **Total Score**: 5/10
- **Recommendation**: Skip unless willing to compete heavily

#### Scenario 2: Low-Value but Accessible
- **Issue**: UnsafeLabs $1 bounty
- **Value**: $1 (1 point)
- **Language**: JavaScript (2 points)
- **Competition**: Low (3 points)
- **Freshness**: 1 day old (2 points)
- **Total Score**: 8/10
- **Recommendation**: Good starting point for experience

#### Scenario 3: Moderate Enhancement
- **Issue**: openai-python retry logging
- **Value**: No bounty but good for portfolio
- **Language**: Python (2 points)
- **Competition**: Low (3 points)
- **Freshness**: Recent (2 points)
- **Total Score**: 7/10
- **Recommendation**: Good contribution opportunity

### Lessons Learned

1. **Freshness Matters**: Most high-value bounties get claimed quickly
2. **Language Alignment**: Target languages reduce scope of work
3. **Competition is Key**: Even high-value bounties may not be worth the effort
4. **Portfolio Building**: Enhancement issues can be valuable for reputation
5. **Authentication**: Environment tokens can interfere with GitHub CLI
6. **Issue vs PR Confusion**: User may reference "PR #3180" when they mean issue #3180. Always verify with `gh pr view` first; if it fails, try `gh issue view`. Issues and PRs share number spaces in GitHub.
7. **Mass-created bounty farms**: When 15+ bounty issues appear from one repo within 2 minutes, it's likely a bounty farm or agent-specific program. Check labels for "Autonomous Agents Only" or "crypto-eligible" as warning signs.

### Best Practices

1. **Run searches at different times** - bounties get claimed quickly
2. **Check both USD and point-based bounties** - some point systems convert well
3. **Evaluate competition before diving in** - save time on oversubscribed bounties
4. **Consider portfolio value** - sometimes free contributions build reputation
5. **Track patterns** - certain repositories consistently post good bounties