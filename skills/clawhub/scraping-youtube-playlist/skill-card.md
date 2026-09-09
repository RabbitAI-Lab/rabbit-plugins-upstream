## Description:

Extracts video metadata from YouTube playlists using apidojo's YouTube Playlist Scraper on Apify for export or downstream analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content curators, educators, and channel analysts use this skill to collect YouTube playlist video metadata for reporting, export, and downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Playlist URLs, search keywords, and actor run inputs are sent to Apify under the user's APIFY_TOKEN.

Mitigation: Use the skill only when those inputs are appropriate to share with Apify and avoid submitting sensitive playlist or keyword data.

Risk: Very large playlists can produce long runs or large outputs.

Mitigation: Set maxItems to cap collection size before running the actor.

Risk: Saving CSV or JSON output can overwrite or confuse existing local result files.

Mitigation: Choose explicit output filenames and review the target path before saving results.

Risk: Private, deleted, or auto-generated mix playlists may return empty, errored, or different results.

Mitigation: Check the playlist URL and report private or unavailable playlists clearly to the user.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/scraping-youtube-playlist)
- [Apify actor runs API endpoint](https://api.apify.com/v2/acts/apidojo~youtube-playlist-scraper/runs)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files, Guidance]

**Output Format:** [Markdown with inline bash code blocks; optional CSV or JSON result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return video title, URL, view count, like count, duration, channel information, description, status, keywords, live/private flags, and thumbnails.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
