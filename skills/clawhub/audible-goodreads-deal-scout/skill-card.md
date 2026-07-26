## Description: <br>
Evaluate an Audible daily promotion against Goodreads public score, optional Goodreads CSV shelves, optional freeform reading notes, optional delivery rules, and manual Want-to-Read discount scans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lenpr](https://clawhub.ai/user/lenpr) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to evaluate Audible daily deals and Goodreads Want-to-Read discounts against public ratings, optional Goodreads shelves, optional reading notes, and delivery preferences. It reports recommendation opportunities and does not make purchases, redeem credits, or manage subscriptions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read configured Goodreads CSV files, notes, generated artifacts, cache, and state. <br>
Mitigation: Point configuration only at files intended for this workflow and use privacyMode minimal when personal notes or reviews should not be used in the model-facing fit step. <br>
Risk: Optional Audible authentication stores sensitive local token fields for member-visible price checks. <br>
Mitigation: Avoid Audible auth unless member-visible prices are needed, keep the auth file private, do not paste or publish it, and use status checks that avoid exposing token values. <br>
Risk: Delivery and scheduled execution can send messages or run unattended on an OpenClaw host. <br>
Mitigation: Enable delivery or cron only on a trusted host and trusted channel, and disable automation or delivery when it is not needed. <br>
Risk: Audible pricing can be hidden, ambiguous, or member-specific, so a reported discount may need human review. <br>
Mitigation: Treat hidden, unknown, or needs-review pricing as uncertainty and make purchase decisions manually outside the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/lenpr/skills/audible-goodreads-deal-scout) <br>
- [Publisher profile](https://clawhub.ai/user/lenpr) <br>
- [Project homepage from ClawHub metadata](https://github.com/lenpr/audible-goodreads-deal-scout) <br>
- [README](artifact/README.md) <br>
- [Trust and Data Access](artifact/TRUST.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, shell commands, JSON runtime contracts, and optional Markdown or JSON recommendation reports] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write configuration, state, reports, artifacts, cache files, optional delivery messages, and optional scheduled-run entries in configured locations.] <br>

## Skill Version(s): <br>
0.1.18 (source: server release evidence, CHANGELOG, package __version__) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
