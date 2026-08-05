## Description: <br>
Use when the user wants to check restaurant availability or make, change, or cancel a table reservation at a restaurant that books through easyTable (a book.easytable.com/book/?id=<id> widget). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to inspect easyTable restaurant availability and manage reservations through the user's own browser session. It supports listing booking areas, dates, and times, finding bookings by phone number, and creating, modifying, or canceling reservations after confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill acts through the user's open browser session via the fetchproxy extension. <br>
Mitigation: Install and pair the extension only when comfortable with that browser-session access, and keep the booking tab scoped to the intended restaurant. <br>
Risk: Reservation create, modify, and cancel actions can change real bookings. <br>
Mitigation: Review the dry-run preview first and re-run with confirm: true only when the requested booking change is correct. <br>
Risk: Create and modify actions depend on a single-use Turnstile token from the booking tab. <br>
Mitigation: Keep the booking widget open and loaded before confirming; reload the tab and retry if the token has expired. <br>


## Reference(s): <br>
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy) <br>
- [easyTable booking widget](https://book.easytable.com/book/?id=<restaurantId>) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, Configuration instructions] <br>
**Output Format:** [Markdown guidance with tool-call names, parameters, and confirmation prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Write actions are confirm-gated; create and modify require an open, loaded easyTable booking tab with a fresh Turnstile token.] <br>

## Skill Version(s): <br>
0.2.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
