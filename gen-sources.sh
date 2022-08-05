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
git clone "${GIT_URL}" "${SOURCE_NAME}"

pushd "${SOURCE_NAME}"
# replace ffmpeg source with Github mirror for speed
git submodule set-url "extra/ffmpeg" "https://github.com/FFmpeg/FFmpeg.git"
# pull submodules
git submodule update --init --recursive
# switch to tagged version
git checkout "${TAG}"
popd

# generate archive
tar -caf "${TARBALL_NAME}" "${SOURCE_NAME}"

# move output out of this dir
mv "${SPEC_NAME}" "${TARBALL_NAME}" ../
