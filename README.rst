.. contents::

Introduction
============

Plonesocial.microblog is part of the `plonesocial suite`_.

This package provides a building block for Plone integrators who want to create a custom social business solution in Plone.

If you're an end-user looking for a pre-integrated solution,
you should install `plonesocial.suite`_ instead.


plonesocial.microblog
=====================

Plonesocial.microblog uses plone.app.discussion to store microblog status updates in an annotation on the Site Root.

This component provides only the status update form and storage. To display the stored microblog messages, use `plonesocial.activitystream`_ in combination with plonesocial.microblog, or install the full `plonesocial.suite`_.

Plonesocial.microblog provides a microblogging solution for Plone using core content types only, without any external dependencies. It does not require an external service and can be set up and run with a normal Plone buildout configuration.

This simplicity also has its downside: this native solution will not be as scalable as a solution that uses an external service. Take a look at the jarn.xmpp.* or collective.kwetter solutions for large-scale microblogging in Plone with very many users. 

That said, the intention is to make this native solution as fast and as scalable as possible. Work is currently in progress to introduce plone.app.async support.

status
------

Alpha. This package is under active development and changes in backward-incompatible and forward-incompatible ways.

Async support is under development but currently breaks. Normal installation without plone.app.async works just fine.


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

