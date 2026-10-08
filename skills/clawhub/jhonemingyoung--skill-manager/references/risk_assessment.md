# Risk Assessment Reference Guide

## Risk Level Definitions

### 🟢 Low Risk
- Purely local file operations (read, convert, format)
- No network requests
- No privilege escalation required
- No sensitive data access
- Code from official or verified sources

### 🟡 Medium Risk
- Involves network requests (API calls, data queries)
- Requires API Key or configuration items
- Can modify local files
- Depends on external runtime environments
- Community-maintained skills

### 🔴 High Risk
- Involves data sending / uploading / publishing
- Requires OAuth or admin privileges
- Can execute system commands (sudo, chmod)
- Contains credential handling (token, password, secret)
- Can delete files or perform destructive operations
- Unknown source or unverified code

## Platform Source Trustworthiness

| Platform | Trust Level | Notes |
|----------|-------------|-------|
| SkillHub official repository | ⭐⭐⭐⭐⭐ | Officially reviewed, highest security |
| skills.sh curated | ⭐⭐⭐⭐ | Community-curated, high quality |
| GitHub well-known organizations | ⭐⭐⭐⭐ | e.g. vercel-labs, ComposioHQ, etc. |
| GitHub individual developers | ⭐⭐⭐ | Check star count and update frequency |
| npm public packages | ⭐⭐ | Requires additional dependency chain review |
| Unknown sources | ⭐ | Not recommended for installation |

## Pre-Installation Checklist

1. [ ] Confirm skill source is trustworthy
2. [ ] Read SKILL.md to understand functionality scope
3. [ ] Check script content for dangerous operations
4. [ ] Verify required permissions are reasonable
5. [ ] Check that network request targets are explicit
6. [ ] Evaluate overlap with existing skills
