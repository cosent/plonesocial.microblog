.. contents::

Introduction
============

Plonesocial.microblog is part of the `plonesocial suite`_.

This package provides a building block for Plone integrators who want to create a custom social business solution in Plone.

If you're an end-user looking for a pre-integrated solution, you should install `plonesocial.suite`_ instead.


plonesocial.microblog
=====================

Plonesocial.microblog provides a 'native' Plone microblogging solution that stores status updates in a performance-optimized site utility.

This component provides only the status update form and storage. To display the stored microblog messages, use `plonesocial.activitystream`_ in combination with plonesocial.microblog, or install the full `plonesocial.suite`_.

Plonesocial.microblog provides a microblogging solution for Plone using core content types only, without any external dependencies. It does not require an external service and can be set up and run with a normal Plone buildout configuration.

The intention is to make this native solution as simple and as fast as possible. The current implementation can handle more than 100 new messages per second in a stock Plone installation on outdated hardware.

status
------

Alpha. This package is under active development and changes in backward-incompatible and forward-incompatible ways. That said, it is usable out of the box.


Plonesocial
===========

Plonesocial consists of:

`plonesocial.suite`_
 An out-of-the-box social business experience integrating all plonesocial.* packages.
 If you're an end user, this is what you're looking for.

`plonesocial.microblog`_
 Status updates

`plonesocial.activitystream`_
 Lists content changes, discussion replies, and status updates

plonesocial.network
 Follow/unfollow of users

plonesocial.like
 Favoriting of content

`plonesocial.buildout`_
 Developer buildout. Not a Python package. Intended for Plonesocial developers only.

.. _plonesocial suite: https://github.com/cosent/plonesocial.suite
.. _plonesocial.microblog: https://github.com/cosent/plonesocial.microblog
.. _plonesocial.activitystream: https://github.com/cosent/plonesocial.activitystream
.. _plonesocial.suite: https://github.com/cosent/plonesocial.suite
.. _plonesocial.buildout: https://github.com/cosent/plonesocial.buildout

