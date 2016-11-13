
# fixme rewrite update mechanism to use this to update all(?) extensions
# todo: add support for versioning based on git head hash

import sys
import clr

from ..config import HOME_DIR

from ..git import git

from System import DateTime, DateTimeOffset



r = git.Repository(HOME_DIR)

print r.Head.Tip.Id.Sha
print r.Head.Tip.Message

# options = git.PullOptions()
# options.FetchOptions = git.FetchOptions()

options = git.FetchOptions()

up = git.UsernamePasswordCredentials()
up.Username = 'eirannejad'
up.Password = 'ehsan2010'


def hndlr(url, uname, types):
    return up


options.FetchOptions.CredentialsProvider = git.Handlers.CredentialsHandler(hndlr)
sig = git.Signature('eirannejad', 'eirannejad@gmail.com', DateTimeOffset(DateTime.Now))

r.Network.Pull(sig, options)
