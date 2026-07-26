-- Batch processing summary table
-- Tracks one row per directory batch run so multi-video jobs are auditable.

create table batch_runs (
  id uuid default gen_random_uuid() primary key,
  created_at timestamp with time zone default now() not null,
  updated_at timestamp with time zone default now() not null,
  user_id uuid references profiles(id) not null,
  source_directory text not null,
  total_videos integer not null default 0,
  succeeded integer not null default 0,
  failed integer not null default 0,
  status text default 'processing' check (status in ('processing', 'completed', 'completed_with_errors', 'failed')),
  metadata jsonb default '{}'::jsonb
);

alter table batch_runs enable row level security;

create policy "Users can view their own batch runs" on batch_runs
  for select using ((select auth.uid()) = user_id);
create policy "Users can create their own batch runs" on batch_runs
  for insert with check ((select auth.uid()) = user_id);
create policy "Users can update their own batch runs" on batch_runs
  for update using ((select auth.uid()) = user_id);

-- Link processed videos back to their batch (nullable for single-video runs).
alter table video_assets
  add column batch_id uuid references batch_runs(id) on delete set null;

-- Persist the derived category on each generated wiki page for grouped publishing.
alter table wiki_pages
  add column category text;
