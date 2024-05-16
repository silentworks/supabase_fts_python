create table movies (
  id uuid primary key default gen_random_uuid(),
  title text,
  rating text,
  description text
);

-- enable RLS (movies table)
alter table public.movies enable row level security;

-- Policies (movies table)
create policy "allow select for all users" on public.movies 
as permissive for select 
to public
using (true);