# ------------------------------------------------------------------------------
# GitHub Actions scripts 
# Copyright(c) pgRouting Contributors
#
# Main configuration
# ------------------------------------------------------------------------------

cmake -DHTML=ON -DJA=ON -@OSGeoLiveDoc_DEBUG=ON ..
make
cd ..
bash scripts/clean-images.sh
touch build/doc/_build/html/.nojekyll # needed for gh pages to keep dirs starting with _
du -h build/doc/_build/html
