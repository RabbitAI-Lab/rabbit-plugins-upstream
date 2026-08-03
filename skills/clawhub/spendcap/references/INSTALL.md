# Install SpendCap

1. Run `bash "{baseDir}/scripts/bootstrap-receipt.sh"`.
2. If the script reports `RECEIPT_CONNECTION_REUSED`, do not start another authorization flow.
3. Otherwise show the exact Receipt authorization URL and wait for the owner to approve it.
4. Complete the localhost callback with the printed clipboard-helper command.
5. Verify that the Receipt connection exposes exactly eight universal tools.
6. Open the attributed owner page printed by the script and ask the owner to select the connected
   app, choose limits, and create or confirm its SpendCap.
7. Read the saved limits back from Receipt before stating that SpendCap is active.

Do not browse the seller catalogue, request a quote, use launch credit, call `receipt_purchase`,
create a hold or reservation, or make any provider call as part of setup.
