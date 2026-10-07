# Event Callback Planner

Version 1.2.0. Python >=3.10; standard library only.

This artifact is the complete probe: identify the input, compute the business result,
write the local business artifact, and -- when configured -- perform the real declared
action (send the message / register or submit the record).

```sh
python scripts/run.py --input examples/request.json --output-dir ./workspace
```

Real delivery is opt-in:

- Message sends: set CLAWHUB_SMTP_HOST, CLAWHUB_SMTP_PORT and CLAWHUB_MAIL_FROM (or pass --delivery-config).
- Registration / submission effects: set CLAWHUB_DELIVERY_ENDPOINT (or pass --delivery-config).

The run returns an `effect` receipt for the local business artifact and a `delivery`
receipt with the real outcome (sent/delivered/failed/unconfigured). Without configuration
the business record is kept locally and no external service is contacted. Errors are
reported through a nonzero exit.
