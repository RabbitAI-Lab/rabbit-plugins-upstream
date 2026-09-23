## Description:

Discogs Sync helps agents add, remove, list, and bulk-sync Discogs wantlist or collection entries, search marketplace pricing, and authenticate with a Discogs personal access token against api.discogs.com.

This skill is ready for commercial/non-commercial use.

## Publisher:

[khaney64](https://clawhub.ai/user/khaney64)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Discogs wantlists and collections from album metadata, Discogs IDs, or CSV/JSON inputs. It is also useful for checking Discogs marketplace pricing before buying or cataloging records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Discogs personal access token that can read and modify the user's wantlist or collection.

Mitigation: Prefer DISCOGS_USER_TOKEN over storing a token on disk, never run interactive auth on the user's behalf, and revoke the token from Discogs if it may be compromised.

Risk: Remove and sync operations can delete wantlist or collection entries when confirmed.

Mitigation: Preview removals without --yes, use --dry-run for sync changes, show the resolved targets to the user, and only rerun with --yes after explicit approval.

Risk: The skill writes local config and cache files under ~/.discogs-sync/ and relies on pinned Python dependencies.

Mitigation: Review the local cache/config behavior before deployment and update pinned dependencies before regular use when security updates are available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/khaney64/skills/discogs-sync)
- [Discogs developer token settings](https://www.discogs.com/settings/developers)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; command output may be terminal tables or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and a Discogs personal access token supplied through DISCOGS_USER_TOKEN or one-time local authentication.]

## Skill Version(s):

0.1.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
