
#include <bits/stdc++.h>
using namespace std;

bool vis[12];
vector<vector<int> >adj(12,vector<int>(12,0));
vector<int>dis(12,-1);

bool bfs(int node){
    queue<int>q;
    q.push(node);
    vis[node]=true;
    dis[node]=0;
    while(!q.empty()){
        node=q.front();
        q.pop();
        for(int i=0;i<=adj[node].size();i++){
            if(adj[node][i]){
                if(!vis[i]){
                    q.push(i);
                    vis[i]=true;
                    dis[i]=dis[node]+1;
                }
            }
        }
    }
    for(int i=1; i<=8; i++){
        if(vis[i] == false){
            return false;
        }
    }
    return true;
}

int main()
{
    int a,b;
    memset(vis,false,sizeof(vis));
    for(int i=0;i<9;i++){
        cin>>a>>b;
        adj[a][b]=1;
        adj[b][a]=1;
    }
    if(bfs(1)){
        cout<<"true";
    }
    else{
        cout<<"false";
    }
    
    return 0;
}
