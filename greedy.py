import copy
import itertools

STATIONS: dict[str, set[str]] = {}  # represents radio stations and states that they cover
STATIONS['kone'] = {'id', 'nv', 'ut'}
STATIONS['ktwo'] = {'wa', 'id', 'mt'}
STATIONS['kthree'] = {'or', 'nv', 'ca'}
STATIONS['kfour'] = {'nv', 'ur'}
STATIONS['kfive'] = {'ca', 'az'}

STATES_NEEDED: set[str] = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}  # states that need to be cover

def find_optimal_stations(stations: dict[str, set[str]], states_needed: set[str]) -> set[str]:
    """
    Finds optimal set of radio stations that can cover all the needed states.
    Uses 'greedy' approach, choosing locally optimal station on each step to get globally optimal solution.
    Complexity: O()
    """
    if len(stations) == 0 or sum(len(states) for states in stations.values()) == 0:
        raise ValueError('No stations have been provided')

    if not set(itertools.chain.from_iterable(stations.values())).issuperset(states_needed):
        raise ValueError("Given stations can't cover all needed states")

    optimal_stations_to_cover_all_states_needed: set[str] = set()

    states_needed_copy = copy.copy(states_needed)
    while states_needed_copy:
        best_station: str | None = None
        states_covered: set[str] = set()
        
        for station, states in stations.items():
            if station in optimal_stations_to_cover_all_states_needed:
                continue

            covered = states_needed_copy & states

            if len(covered) > len(states_covered):
                best_station = station
                states_covered = states
        
        states_needed_copy -= states_covered
        optimal_stations_to_cover_all_states_needed.add(best_station)

    return optimal_stations_to_cover_all_states_needed

assert ', '.join(sorted(find_optimal_stations(STATIONS, STATES_NEEDED))) == 'kfive, kone, kthree, ktwo'

try:
    find_optimal_stations(stations={'vone': {'id', 'nv', 'ut'}, 'vtwo': {'ca', 'az'}}, states_needed=STATES_NEEDED)
except ValueError as e:
    unsufficient_coverage_error = True
    err_msg = str(e)
else:
    unsufficient_coverage_error = False
    err_msg = None

assert unsufficient_coverage_error
assert err_msg == "Given stations can't cover all needed states"

try:
    find_optimal_stations(stations={'zone': {}, 'ztwo': {}}, states_needed=STATES_NEEDED)
except ValueError as e:
    no_stations_error = True
    err_msg = str(e)
else:
    no_stations_error = False
    err_msg = None

assert no_stations_error
assert err_msg == 'No stations have been provided'

assert ', '.join(sorted(find_optimal_stations(stations=STATIONS, states_needed={}))) == ''
