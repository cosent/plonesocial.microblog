Introduction
============

Plonesocial.microblog is part of the `plonesocial suite`_.

If you're an integrator or end-user looking for a pre-integrated solution, you should install `plonesocial.suite`_.

This package, plonesocial.microblog, provides a building block for Plone developers who want to create a custom social business solution in Plone.
You normally wouldn't want to modify this unless you know exactly what you're doing.


plonesocial.microblog
=====================

Plonesocial.microblog provides a 'native' Plone microblogging solution that stores status updates in a performance-optimized site utility.

This component provides only the status update form and storage. To display the stored microblog messages, use `plonesocial.activitystream`_ in combination with plonesocial.microblog, or install the full `plonesocial.suite`_.

Plonesocial.microblog provides a microblogging solution for Plone using core content types only, without any external dependencies. It does not require an external service and can be set up and run with a normal Plone buildout configuration.

The intention is to make this native solution as simple and as fast as possible. The current implementation can handle hundreds of new messages per second in a stock Plone installation on outdated hardware. It achieves this by using batched async commits (without using ``plone.app.async``) and by not indexing status updates in ZCatalog. Instead, custom indexes on time, author and tags are provided.

bugs
----

Uninstalling either plonesocial.microblog or `plonesocial.network`_ removes both utilities, deleting all data.

TODO
----

Indexing @username mentions for integration with `plonesocial.network`_.


.. _plonesocial suite: https://github.com/cosent/plonesocial.suite
.. _plonesocial.suite: https://github.com/cosent/plonesocial.suite
.. _plonesocial.activitystream: https://github.com/cosent/plonesocial.activitystream
.. _plonesocial.network: https://github.com/cosent/plonesocial.network


