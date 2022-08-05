#!/usr/bin/env bash

########## BUMP ##########
VER="1.0.2"
##########################

set -ex

GIT_URL="https://github.com/wirow-io/wirow-server.git"
SOURCE_NAME="wirow-${VER}"
TAG="v${VER}"
TARBALL_NAME="${TAG}.tar.gz"
SPEC_NAME="wirow.spec"

# work within this dir
cd $(dirname "$0")

# clone
git clone --recurse-submodules "${GIT_URL}" "${SOURCE_NAME}"

# switch to tagged version, then remove VCS info
pushd "${SOURCE_NAME}"
git checkout "${TAG}"
rm -rf .git
popd

# generate archive
tar -caf "${TARBALL_NAME}" "${SOURCE_NAME}"

# move output out of this dir
mv "${SPEC_NAME}" "${TARBALL_NAME}" ../
