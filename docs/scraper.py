from github import Github
import calendar, time

#access token
g = Github("**GITUB API KEY HERE**")

#get a repo by name
repo = g.get_repo("**TARGETED REPO HERE**")

#get the pull requests
pulls = repo.get_pulls(state = 'all')
prList = []
step = 250
for i in range(0, pulls.totalCount, step):
    prList = []

    #check how many API calls you have remaining
    rl = g.get_rate_limit()
    rl_core = rl.core
    rl_search = rl.search
    
    core_rate_limit = rl.core
    reset_timestamp = calendar.timegm(core_rate_limit.reset.timetuple())
    sleep_time = reset_timestamp - calendar.timegm(time.gmtime()) + 5  # add 5 seconds to be sure the rate limit has been reset
    print(f"{i} current step, {rl_core.remaining} API calls remaining, {sleep_time} time to reset")
    if rl_core.remaining > 500:
        #print("not sleeping")
        for pr in pulls[i:i+step]: 
            #print(pr.number)
            prList.append((pr.number, pr.closed_at, pr.created_at, pr.state, pr.title.replace(',', ' '),
                           pr.merged_at, pr.is_merged(), pr.html_url))
        
        with open(f"D:\**PATH**\\**REPO-data**{i}.csv", 'w', encoding="utf-16") as f:
            for p in prList:
                f.write(",".join([str(x).strip(",") for x in p]) + "\n")
    else:
        print(f"slep until {sleep_time}")
        time.sleep(sleep_time)

print(prList)
