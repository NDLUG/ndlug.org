+++
categories = ["lug"]
date = "2017-11-28T13:09:20-04:00"
description = "Guide for using the new-old ND web hosting"
draft = false
tags = ["how to"]
title = "ND Web Hosting How To"
toc = false

+++

If you previously maintained your web page by SFTP to webfile.nd.edu,
that no longer works as of 2017/07/25. The new server is accessed by
FTPS (FTP over SSL), and the new instructions tell you to use one of
several graphical FTP clients. But you can use the command-line `lftp`
client.

<!--more-->

# Configure lftp

Edit your `~/.lftprc` to include the following lines:

```
set ftp:ssl-allow true
set ftp:ssl-force true
set ftp:ssl-protect-data true
set ftp:ssl-protect-list true
set ssl:verify-certificate false
```

To do: How to obtain and verify the SSL certificate?

# Connect to the lftp server

```
$ lftp username@www3ftps.nd.edu
```

Note: Do not put `ftps://` before the URL.

# Miscellaneous notes

The new server appears to be HTTPS-only. If you have a `<link
href=...>` tag, make sure that the linked URL uses `https://`, not
`http://`.
