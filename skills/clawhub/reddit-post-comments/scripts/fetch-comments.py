import argparse
import json
import sys


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(description='Generate JS to fetch Reddit post and initial comments')
    parser.add_argument('post_id', help='Reddit post ID (e.g. 1s80pf6)')
    parser.add_argument('--limit', type=int, default=500,
                        help='Max initial comments per fetch (1-500)')
    parser.add_argument('--depth', type=int, default=10,
                        help='Max comment nesting depth to retrieve')
    parser.add_argument('--date-from', dest='date_from', default='',
                        help='Lower date bound for comments ISO-8601 or YYYY-MM-DD')
    parser.add_argument('--date-to', dest='date_to', default='',
                        help='Upper date bound for comments ISO-8601 or YYYY-MM-DD')
    args = parser.parse_args()

    js = f"""
(async () => {{
  try {{
    const postId   = {json.dumps(args.post_id)};
    const limit    = Math.min({args.limit}, 500);
    const depth    = {args.depth};
    const dateFrom = {json.dumps(args.date_from)};
    const dateTo   = {json.dumps(args.date_to)};

    const endpoint = 'https://www.reddit.com/comments/' + postId +
      '.json?limit=' + limit + '&depth=' + depth;

    const resp = await fetch(endpoint, {{ headers: {{ 'Accept': 'application/json' }} }});
    if (!resp.ok) {{
      return JSON.stringify({{ error: true, message: 'HTTP ' + resp.status + ' for post ' + postId }});
    }}
    const data = await resp.json();
    if (!Array.isArray(data) || data.length < 2) {{
      return JSON.stringify({{ error: true, message: 'Unexpected response shape for post ' + postId }});
    }}

    const now  = new Date().toISOString();
    const post = data[0]?.data?.children?.[0]?.data;
    if (!post) {{
      return JSON.stringify({{ error: true, message: 'Post not found or unavailable: ' + postId }});
    }}
    const postUrl = 'https://www.reddit.com' + post.permalink;

    // Recursively flatten comment tree into a flat array
    const flattenComments = (children) => {{
      const result = [];
      for (const c of (children || [])) {{
        if (c.kind !== 't1') continue;
        const d = c.data;
        const ageHours  = Math.round((Date.now() / 1000 - d.created_utc) / 3600 * 10) / 10;
        const isDeleted = d.body === '[deleted]' || d.body === '[removed]' || d.author === '[deleted]';
        const parentKind = (d.parent_id || '').startsWith('t3_') ? 'post' : 'comment';
        result.push({{
          kind: 'comment',
          id: d.id,
          post_id: postId,
          post_url: postUrl,
          parent_id: d.parent_id,
          body: d.body || null,
          author: d.author,
          score: d.score,
          subreddit: d.subreddit || post.subreddit || null,
          created_utc: new Date(d.created_utc * 1000).toISOString(),
          url: 'https://www.reddit.com' + d.permalink,
          permalink: d.permalink,
          canonical_url: 'https://www.reddit.com' + d.permalink,
          old_reddit_url: 'https://old.reddit.com' + d.permalink,
          root_comment_id: d.id,
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
          stickied: d.stickied,
          distinguished: d.distinguished || null,
          is_submitter: d.is_submitter,
          score_hidden: d.score_hidden || false,
          controversiality: d.controversiality || 0,
          depth: d.depth,
          total_awards_received: d.total_awards_received || 0,
          gilded: d.gilded || 0,
          author_fullname: d.author_fullname || null,
          author_flair_text: d.author_flair_text || null,
          author_premium: d.author_premium || false,
          collapsed: d.collapsed || false,
          collapsed_reason: d.collapsed_reason || null,
          collapsed_because_crowd_control: d.collapsed_because_crowd_control || false,
          unrepliable_reason: d.unrepliable_reason || null
        }});
        // Recurse into nested replies
        if (d.replies?.data?.children) {{
          result.push(...flattenComments(d.replies.data.children));
        }}
      }}
      return result;
    }};

    const commentChildren = data[1]?.data?.children || [];
    const moreIds = commentChildren
      .filter(c => c.kind === 'more')
      .flatMap(c => c.data?.children || []);

    let comments = flattenComments(commentChildren);

    // Date filtering (record-level)
    if (dateFrom) {{
      const fromTs = new Date(dateFrom).getTime();
      comments = comments.filter(c => new Date(c.created_utc).getTime() >= fromTs);
    }}
    if (dateTo) {{
      const toTs = new Date(dateTo).getTime();
      comments = comments.filter(c => new Date(c.created_utc).getTime() <= toTs);
    }}

    return JSON.stringify({{
      post_id: postId,
      post_title: post.title || null,
      post_url: postUrl,
      comments: comments,
      more_ids: moreIds,
      count: comments.length,
      has_more: moreIds.length > 0
    }});
  }} catch (e) {{
    return JSON.stringify({{ error: true, message: e.message }});
  }}
}})()
"""
    print(js)


if __name__ == '__main__':
    main()
