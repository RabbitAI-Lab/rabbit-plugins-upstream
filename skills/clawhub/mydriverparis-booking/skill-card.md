## Description: <br>
Get instant quotes and book private chauffeur rides in Paris and across Europe with MyDriverParis, including airport and train station transfers, hourly hire, day trips, and VIP airport Meet & Greet. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[skatch](https://clawhub.ai/user/skatch) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-service agents use this skill to quote and book private chauffeur rides with pickup or drop-off in France. It supports airport and station transfers, city-to-city rides, hourly chauffeur service, private day trips, and VIP airport Meet & Greet bookings. <br>

### Deployment Geography for Use: <br>
Global use for ride requests that start or end in France. <br>

## Known Risks and Mitigations: <br>
Risk: Ride details and passenger contact information are sent to the MyDriverParis remote MCP service. <br>
Mitigation: Collect only the details needed for quoting or booking, confirm the passenger information with the user, and avoid sending unrelated personal data. <br>
Risk: A booking may be misunderstood as confirmed before payment is complete. <br>
Mitigation: Present the Stripe payment link clearly and state that the ride is confirmed only after payment is completed. <br>
Risk: Quotes can expire or become stale. <br>
Mitigation: Use the returned quote details, verify vehicle and price with the user, and rerun the quote flow when the service reports an expired or unknown quote. <br>


## Reference(s): <br>
- [MyDriverParis homepage](https://www.mydriverparis.com) <br>
- [MyDriverParis agent documentation](https://www.mydriverparis.com/llms-full.txt) <br>
- [MyDriverParis MCP server endpoint](https://mcp-mydriverparis.mydriverparis.workers.dev/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance, shell commands, configuration, API calls] <br>
**Output Format:** [Markdown instructions with shell command examples and MCP tool-call guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce quote options and Stripe payment links through the MyDriverParis MCP service; bookings are not confirmed until payment is complete.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
