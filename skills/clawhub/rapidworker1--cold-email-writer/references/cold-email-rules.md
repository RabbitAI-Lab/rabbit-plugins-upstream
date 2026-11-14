# CAN-SPAM rules that decide whether the email lands

Reference for the Cold Email Writer skill. Every limit and rule below is a US-facing constraint the workflow has to respect.

## The elements a commercial email needs

- From, To and Reply-To must identify the real sender and must not be false or misleading.
- The subject line must not be false or misleading and must not fake a Re: or Fwd: prefix.
- The message must carry the sender's valid physical postal address.
- The opt-out must be clear, must work without hoops and must be honored within 10 business days.

## Inbox rules that are not statute

- Gmail requires bulk senders to publish SPF, DKIM and DMARC records and to support one-click unsubscribe.
- Gmail expects a bulk sender's spam rate to stay below 0.3 percent.
- Microsoft 365 judges high-volume senders on authentication and complaint rates, not on volume alone.
- A mailbox that sends the same message to the same person twice degrades fast; one follow-up, then stop.

## State law and records

- California, Colorado, Connecticut, Utah and Virginia require consent for some commercial email, not just opt-out.
- Keep one suppression list and check it before every send.
- Record date, time in ET, the source of the address and the exact copy sent for each contact.
- Text messages are governed by TCPA and generally need prior express written consent.
