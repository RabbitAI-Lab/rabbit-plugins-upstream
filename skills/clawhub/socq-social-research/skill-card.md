## Description: <br>
Research public social-platform content, accounts, keywords, and SEO search data with SocQ. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[socq](https://clawhub.ai/user/socq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to run public social-platform and SEO research through SocQ, including endpoint discovery, credit estimation, asynchronous task submission, polling, pagination, and raw export retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends selected public social URLs, usernames, comments, transcripts, keywords, and domains to SocQ under the user's SocQ account. <br>
Mitigation: Install and use only when that data sharing is acceptable, and handle returned profile, follower, comment, and transcript data as potentially personal information. <br>
Risk: SocQ is credit-metered, so large or cross-platform jobs may consume paid credits. <br>
Mitigation: Check account credits and endpoint billing before large runs, reduce result limits or platform count when scope is unclear, and confirm large jobs before submission. <br>
Risk: API keys can be exposed if placed in prompts, URLs, committed files, or retained shell commands. <br>
Mitigation: Use SOCQ_API_KEY from the process environment or approved local configuration, avoid query-string credentials, and do not place keys in prompts or persisted commands. <br>
Risk: Provider failures, unsupported filters, or early pagination stops can make results incomplete. <br>
Mitigation: Poll tasks to a terminal state, follow pagination to the requested cap, preserve task IDs for resume, and report partial coverage, failed platforms, filters, and collection time. <br>


## Reference(s): <br>
- [SocQ Devtools](https://github.com/SocQAPI/socq-devtools) <br>
- [SocQ Skill on ClawHub](https://clawhub.ai/socq/skills/socq-social-research) <br>
- [Authentication](references/authentication.md) <br>
- [Billing and Cost Control](references/billing.md) <br>
- [Asynchronous Tasks](references/async-tasks.md) <br>
- [Pagination and Files](references/pagination.md) <br>
- [Errors and Recovery](references/errors.md) <br>
- [Cross-platform Research](references/cross-platform.md) <br>
- [Capability Catalog](references/catalog.md) <br>
- [Facebook](references/platforms/facebook.md) <br>
- [Facebook Ad Library](references/platforms/facebook-ad-library.md) <br>
- [Facebook Marketplace](references/platforms/facebook-marketplace.md) <br>
- [Instagram](references/platforms/instagram.md) <br>
- [LinkedIn](references/platforms/linkedin.md) <br>
- [Pinterest](references/platforms/pinterest.md) <br>
- [Reddit](references/platforms/reddit.md) <br>
- [SEO](references/platforms/seo.md) <br>
- [Threads](references/platforms/threads.md) <br>
- [TikTok](references/platforms/tiktok.md) <br>
- [TikTok Shop](references/platforms/tiktok-shop.md) <br>
- [X](references/platforms/x.md) <br>
- [YouTube](references/platforms/youtube.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration values, endpoint guidance, and research summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include SocQ task IDs, pagination cursors, partial-coverage notes, failed platform details, filters, and collection time.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
