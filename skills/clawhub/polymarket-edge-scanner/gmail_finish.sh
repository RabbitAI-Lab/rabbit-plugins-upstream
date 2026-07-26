#!/bin/bash
set -euo pipefail
export MATON_API_KEY="v2.fSIdyoTHcoGKwYQnWcS0DBYQNSBCv-FMrmCNeqjTktG9LgZMjo6UAimFGtHmrmH7ztgXj5f5kHmmzGRcElsYQWHw6hShbxkOsG1JwxBWFO3lfviy1xdpp7vS"
export HOME=/root
MATON="./node_modules/.bin/maton"

mark_read_query() {
    local query="$1"
    echo "Marking read: $query"
    local ids
    ids=$("$MATON" gmail message list -L 50 --query "$query" --json | python3 -c "import sys,json; [print(m['id']) for m in json.load(sys.stdin).get('messages', [])]")
    for id in $ids; do
        echo "  mark read $id"
        "$MATON" gmail message modify "$id" --remove-label UNREAD >/dev/null
        sleep 2
    done
}

add_label_query() {
    local query="$1"
    local label="$2"
    echo "Labeling $label: $query"
    local ids
    ids=$("$MATON" gmail message list -L 50 --query "$query" --json | python3 -c "import sys,json; [print(m['id']) for m in json.load(sys.stdin).get('messages', [])]")
    for id in $ids; do
        echo "  label $id"
        "$MATON" gmail message modify "$id" --add-label "$label" >/dev/null
        sleep 2
    done
}

# Promotions -> mark read
mark_read_query "is:unread from:michaelkorsmail.com"
mark_read_query "is:unread from:mail.checkers.co.za"
mark_read_query "is:unread from:pnp.co.za"
mark_read_query "is:unread from:global.fortinet.com"
mark_read_query "is:unread from:samuraiguitartheory.com"
mark_read_query "is:unread from:firstshop.co.za"
mark_read_query "is:unread from:oldjwauctioneers.com"
mark_read_query "is:unread from:e.sunglasshut.com"
mark_read_query "is:unread from:stevenslateaudio.com"
mark_read_query "is:unread from:fanvue.com"
mark_read_query "is:unread from:onedealaday.co.za"
mark_read_query "is:unread from:premiuminfo.fool.com"
mark_read_query "is:unread from:motley.fool.com subject:Here are OR subject:Did you miss OR subject:briefing"

# Categories -> label
add_label_query "is:unread from:linkedin.com" "Label_13"
add_label_query "is:unread from:indeed.com OR from:pnet.co.za OR from:greenhouse-mail.io OR from:us.greenhouse-jobs.com OR from:monks.com OR from:placementpartner.com OR from:jobstellen.de OR from:glassdoor.com OR from:simplify.hr OR from:orangecyberdefensegroup.teamtailor-mail.com" "Label_15"
add_label_query "is:unread from:fnb.co.za OR from:discoverybank.co.za OR from:discovery.bank OR from:stripe.com OR from:hostinger.com" "Label_14"
add_label_query "is:unread from:udemy.com OR from:udemymail.com" "Label_17"
add_label_query "is:unread from:wordpress@igamingreviews.org OR subject:igaming" "Label_16"
add_label_query "is:unread from:1password.com OR from:accounts.google.com OR from:anthropic.com" "Label_18"

echo "Done."
