import argparse
import json
import sys


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(
        description='Generate JS to fetch additional Reddit comments via morechildren API')
    parser.add_argument('post_id', help='Reddit post ID (e.g. 1s80pf6)')
    parser.add_argument('--children', default='',
                        help='Comma-separated comment IDs from the more_ids field of a previous fetch')
    parser.add_argument('--date-from', dest='date_from', default='',
                        help='Lower date bound for comments ISO-8601 or YYYY-MM-DD')
    parser.add_argument('--date-to', dest='date_to', default='',
                        help='Upper date bound for comments ISO-8601 or YYYY-MM-DD')
    args = parser.parse_args()

    js = f"""
(async () => {{
  try {{
    const postId   = {json.dumps(args.post_id)};
    const children = {json.dumps(args.children)};
    const dateFrom = {json.dumps(args.date_from)};
    const dateTo   = {json.dumps(args.date_to)};

    if (!children || !children.trim()) {{
      return JSON.stringify({{ error: true, message: 'No children IDs provided via --children' }});
    }}

    const endpoint = 'https://www.reddit.com/api/morechildren.json' +
      '?api_type=json&link_id=t3_' + postId +
      '&children=' + encodeURIComponent(children.trim()) +
      '&limit_children=false';

    const resp = await fetch(endpoint, {{ headers: {{ 'Accept': 'application/json' }} }});
    if (!resp.ok) {{
      return JSON.stringify({{ error: true, message: 'HTTP ' + resp.status + ' from morechildren' }});
    }}
    const data = await resp.json();

    if (data.json?.errors?.length) {{
      return JSON.stringify({{ error: true, message: 'API errors: ' + JSON.stringify(data.json.errors) }});
    }}

    const things = data.json?.data?.things || [];
    const now    = new Date().toISOString();

    let comments = things.filter(t => t.kind === 't1').map(t => {{
      const d = t.data;
      const ageHours  = Math.round((Date.now() / 1000 - d.created_utc) / 3600 * 10) / 10;
      const isDeleted = d.body === '[deleted]' || d.body === '[removed]' || d.author === '[deleted]';
      const parentKind = (d.parent_id || '').startsWith('t3_') ? 'post' : 'comment';
      return {{
        kind: 'comment',
        id: d.id,
        post_id: postId,
        post_url: 'https://www.reddit.com/comments/' + postId + '/',
        parent_id: d.parent_id,
        body: d.body || null,
        author: d.author,
        score: d.score,
        subreddit: d.subreddit || null,
        created_utc: new Date(d.created_utc * 1000).toISOString(),
        url: d.permalink ? 'https://www.reddit.com' + d.permalink : null,
        permalink: d.permalink || null,
        canonical_url: d.permalink ? 'https://www.reddit.com' + d.permalink : null,
        old_reddit_url: d.permalink ? 'https://old.reddit.com' + d.permalink : null,
        parent_kind: parentKind,
        is_deleted_or_removed: isDeleted,
        subreddit_id: d.subreddit_id || null,
        subreddit_name_prefixed: d.subreddit_name_prefixed || null,
        edited: d.edited || false,
        retrieved_at: now,
        age_hours: ageHours,
        body_length: (d.body || '').length,
        word_count: (d.body || '').split(/\\s+/).filter(Boolean).length,
        score_per_hour: ageHours > 0.01 ? Math.round(d.score / Math.max(ageHours, 0.01) * 100) / 100 : 0,
        stickied: d.stickied || false,
        distinguished: d.distinguished || null,
        is_submitter: d.is_submitter || false,
        score_hidden: d.score_hidden || false,
        controversiality: d.controversiality || 0,
        depth: d.depth,
        total_awards_received: d.total_awards_received || 0,
        gilded: d.gilded || 0,
        author_fullname: d.author_fullname || null,
        author_flair_text: d.author_flair_text || null,
        author_premium: d.author_premium || false,
        collapsed: d.collapsed || false,
        collapsed_reason: d.collapsed_reason || null
      }};
    }});

    // Date filtering (record-level)
    if (dateFrom) {{
      const fromTs = new Date(dateFrom).getTime();
      comments = comments.filter(c => new Date(c.created_utc).getTime() >= fromTs);
    }}
    if (dateTo) {{
      const toTs = new Date(dateTo).getTime();
      comments = comments.filter(c => new Date(c.created_utc).getTime() <= toTs);
    }}

    // Remaining 'more' items for further batches
    const remainingMore = things
      .filter(t => t.kind === 'more')
      .flatMap(t => t.data?.children || []);

    return JSON.stringify({{
      comments: comments,
      more_ids: remainingMore,
      count: comments.length,
      has_more: remainingMore.length > 0
    }});
  }} catch (e) {{
    return JSON.stringify({{ error: true, message: e.message }});
  }}
}})()
"""
    print(js)


if __name__ == '__main__':
    main()
