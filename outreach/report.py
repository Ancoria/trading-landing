#!/usr/bin/env python3
"""Generate funnel report from outreach tracker CSV."""
import csv
from datetime import date
from collections import Counter

TRACKER = '/Users/zl/trading-landing/outreach/tracker.csv'

def report():
    rows = []
    with open(TRACKER) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    total = len(rows)
    replied = sum(1 for r in rows if r['Replied'].strip().lower() == 'yes')
    calls = sum(1 for r in rows if r['Call Booked'].strip().lower() == 'yes')
    closed = sum(1 for r in rows if r['Closed'].strip().lower() == 'yes')
    
    # Revenue
    revenue = sum(float(r['Revenue']) for r in rows if r['Revenue'].strip())
    
    # By platform
    platforms = Counter(r['Platform'].strip() for r in rows if r['Platform'].strip())
    replies_by_platform = Counter(
        r['Platform'].strip() for r in rows 
        if r['Replied'].strip().lower() == 'yes'
    )
    
    # By category
    categories = Counter(r['Category'].strip() for r in rows if r['Category'].strip())
    
    # Today's activity
    today = str(date.today())
    today_sent = sum(1 for r in rows if r['Date Sent'].strip() == today)
    
    print(f"""
=== FUNNEL REPORT ===
Date: {today}

Activity
  Total DMs sent: {total} (today: {today_sent})
  Replies: {replied} ({replied/total*100:.0f}% reply rate)
  Calls booked: {calls} ({calls/total*100:.0f}% conversion)
  Closed: {closed} ({closed/total*100:.0f}% close rate)
  Revenue: ${revenue:.0f}

By Platform
  {', '.join(f'{p}: {c}' for p,c in platforms.most_common())}

By Category
  {', '.join(f'{cat}: {c}' for cat,c in categories.most_common())}

Reply Rate by Channel
  {', '.join(f'{p}: {replies_by_platform.get(p,0)}/{platforms[p]}' for p in platforms)}
""")

if __name__ == '__main__':
    report()
