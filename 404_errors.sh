#!/bin/bash
grep "404" /var/log/apache2/access.log > /mnt/shared/windows/404_errors.log
