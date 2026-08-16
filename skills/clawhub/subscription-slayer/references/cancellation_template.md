# Cancellation Email Template Reference

Subscription Slayer generates ready-to-send cancellation emails. This document explains the template structure and how to customise it.

## Standard Template

```
To: support@{company}.com
Subject: Cancellation Request — {name} Subscription (Account #[YOUR ACCOUNT ID])

Dear {Company} Customer Support,

I am writing to formally request the cancellation of my {name} subscription,
effective immediately.

Account details:
  - Service: {name}
  - Account email: [YOUR EMAIL]
  - Account/Member ID: [YOUR ACCOUNT ID]
  - Name on account: [YOUR NAME]

Please process this cancellation and confirm via email that:
1. My subscription has been cancelled and will not be renewed.
2. No further charges will be made to my payment method.
3. Any applicable pro-rated refund for the unused portion of my billing
   cycle is processed.

If you require any additional information to process this request, please
contact me at [YOUR EMAIL].

I expect written confirmation of the cancellation within 5 business days,
as required by consumer protection regulations.

Sincerely,
[YOUR NAME]
[YOUR EMAIL]
```

## Placeholders to Replace

Before sending, replace these placeholders:

| Placeholder | Replace with |
|-------------|-------------|
| `[YOUR EMAIL]` | Your account email address |
| `[YOUR ACCOUNT ID]` | Your subscription/account/member ID |
| `[YOUR NAME]` | Your full name as it appears on the account |

## Email Address Inference

The script infers a support email from the subscription name:
- Company name is extracted as the first word
- Domain is generated as `{company.lower()}.com`
- Email is `support@{domain}`

This is a best guess. **Always verify the correct email address** by checking:
1. The company's website "Contact Us" page
2. Your account settings or billing page
3. Previous correspondence from the company

## Customising Templates

### Adding company-specific details

Some companies have specific cancellation requirements. You can modify the template in `scripts/subscription_tracker.py`:

```python
EMAIL_TEMPLATE = """To: {email}
Subject: {subject}

Dear {company} Cancelations Team,
...
"""
```

### Different tones

For a more assertive tone:
```
I am exercising my right to cancel under the terms of service.
Please confirm within 3 business days.
```

For a friendlier tone:
```
I've enjoyed using {name} but need to cancel for budget reasons.
Could you please process this at your earliest convenience?
```

## Legal Considerations

The template references "consumer protection regulations" which generally require companies to:
- Process cancellations within a reasonable timeframe (typically 3–5 business days)
- Provide written confirmation
- Not charge for services after cancellation date
- Process any applicable refunds

Specific regulations vary by jurisdiction:
- **US**: FTC's "Click to Cancel" rule (effective 2024) requires easy cancellation
- **EU**: Consumer Rights Directive mandates 14-day cancellation rights
- **UK**: Consumer Contracts Regulations provide similar protections
- **Australia**: Australian Consumer Law provides cancellation rights

## After Sending

1. **Keep the sent email** as proof of your cancellation request.
2. **Note the date** you sent it — start counting the 5-day window.
3. **Check your next billing statement** to confirm no charges were made.
4. **If no response within 5 days**: Follow up, then dispute the charge with your bank/credit card if needed.
5. **If still being charged**: File a complaint with your local consumer protection agency.
