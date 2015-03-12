Introduction
============

Plonesocial.microblog is part of the `ploneintranet suite`_.

If you're an integrator or end-user looking for a pre-integrated solution, you should install `ploneintranet.suite`_.

This package, ploneintranet.microblog, provides a building block for Plone developers who want to create a custom social business solution in Plone.
You normally wouldn't want to modify this unless you know exactly what you're doing.

Credits
-------

|Cosent|_

This package is maintained by Cosent_.

.. _Cosent: http://cosent.nl
.. |Cosent| image:: http://cosent.nl/images/logo-external.png 
                    :alt: Cosent


ploneintranet.microblog
=====================

Plonesocial.microblog provides a 'native' Plone microblogging solution that stores status updates in a performance-optimized site utility.

This component provides only the status update form and storage. To display the stored microblog messages, use `ploneintranet.activitystream`_ in combination with ploneintranet.microblog, or install the full `ploneintranet.suite`_.

Plonesocial.microblog provides a microblogging solution for Plone using core content types only, without any external dependencies. It does not require an external service and can be set up and run with a normal Plone buildout configuration.

The intention is to make this native solution as simple and as fast as possible. The current implementation can handle hundreds of new messages per second in a stock Plone installation on outdated hardware. It achieves this by using batched async commits (without using ``plone.app.async``) and by not indexing status updates in ZCatalog. Instead, custom indexes on time, author and tags are provided.


workspaces
----------

This package provides the "Hosts a local microblog" behavior that can be applied to Dexterity content. When applied to an context, it enables microblogging and activitystreams that are local to that context.

You can also use this on Archetypes content by marking an object as providing the IMicroblogContext interface. An example taken from ploneintranet.suite::

        # enable local microblog
        directlyProvides(portal.workspace, IMicroblogContext)


upgrades
--------

An upgrade step is provided to add the UUID index introduced in 0.5 to older installations.

Build status
------------

Unit tests
~~~~~~~~~~

.. image:: https://secure.travis-ci.org/cosent/ploneintranet.microblog.png
    :target: http://travis-ci.org/cosent/ploneintranet.microblog
.. image:: http://jenkins.ploneintranet.net/buildStatus/icon?job=Plone%20Social%20Microblog
    :target: http://jenkins.ploneintranet.net/job/Plone%20Social%20Microblog/

Robot tests for Plone Social and Plone Intranet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: http://jenkins.ploneintranet.net/buildStatus/icon?job=Plone%20Social%20Suite
   :target: http://jenkins.ploneintranet.net/job/Plone%20Social%20Suite%20Master/badge/

.. image:: http://jenkins.ploneintranet.net/buildStatus/icon?job=Plone%20Intranet%20Suite%20Master
   :target: http://jenkins.ploneintranet.net/job/Plone%20Intranet%20Suite%20Master/badge/

bugs
----

Uninstalling either ploneintranet.microblog or `ploneintranet.network`_ removes both utilities, deleting all data.

Roadmap
-------

An extensive roadmap_ for the ploneintranet suite is available on github.

.. _ploneintranet suite: https://github.com/cosent/ploneintranet.suite
.. _ploneintranet.suite: https://github.com/cosent/ploneintranet.suite
.. _ploneintranet.activitystream: https://github.com/cosent/ploneintranet.activitystream
.. _ploneintranet.network: https://github.com/cosent/ploneintranet.network
.. _roadmap: https://github.com/cosent/ploneintranet.suite/wiki



Copyright (c) Plone Foundation
------------------------------

This package is Copyright (c) Plone Foundation.

Any contribution to this package implies consent and intent to irrevocably transfer all 
copyrights on the code you contribute, to the `Plone Foundation`_, 
under the condition that the code remains under a `OSI-approved license`_.

To contribute, you need to have signed a Plone Foundation `contributor agreement`_.
If you're `listed on Github`_ as a member of the Plone organization, you already signed.

.. _Plone Foundation: https://plone.org/foundation
.. _OSI-approved license: http://opensource.org/licenses
.. _contributor agreement: https://plone.org/foundation/contributors-agreement
.. _listed on Github: https://github.com/orgs/plone/people
