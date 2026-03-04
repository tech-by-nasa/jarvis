import git

class GitHubManager:
    def __init__(self, path):
        self.repo = git.Repo(path)

    def commit_and_push(self, message):
        self.repo.git.add(A=True)
        self.repo.index.commit(message)
        origin = self.repo.remote(name='origin')
        origin.push()
        return "Changes deployed to GitHub, sir."
